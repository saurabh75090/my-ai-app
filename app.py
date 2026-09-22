import streamlit as st
from google import genai

# -------------------------
# App settings
# -------------------------

st.set_page_config(
    page_title="My AI",
    page_icon="🤖"
)

st.title("🤖 My AI")
st.caption("My free online AI assistant")

# Gemini se connection
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# -------------------------
# Chat history
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# Sidebar
# -------------------------

with st.sidebar:

    st.title("My AI")

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.write("Model: Gemini 3.8 Flash")
    st.write("Online AI")

# -------------------------
# Purane messages dikhana
# -------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------
# ChatGPT jaisa input box
# -------------------------

prompt = st.chat_input("Message My AI...")

if prompt:

    # User message save
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # User message screen par
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            # Current conversation ko text me convert karo
            conversation = ""

            for message in st.session_state.messages:

                if message["role"] == "user":
                    conversation += "User: " + message["content"] + "\n"

                else:
                    conversation += "Assistant: " + message["content"] + "\n"

            conversation += "Assistant:"

            # Gemini ko conversation bhejo
            interaction = client.interactions.create(
                model="gemini-3.8-flash",
                input=conversation
            )

            # Gemini ka answer
            answer = interaction.output_text

            st.markdown(answer)

    # AI answer history me save
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )