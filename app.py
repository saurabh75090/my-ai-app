import streamlit as st
from google import genai
from google.genai import errors


# -------------------------
# APP SETTINGS
# -------------------------

st.set_page_config(
    page_title="My AI",
    page_icon="🤖"
)

st.title("🤖 My AI")
st.caption("My free online AI assistant")


# -------------------------
# GEMINI CONNECTION
# -------------------------

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)


# -------------------------
# CHAT HISTORY
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# -------------------------
# SIDEBAR
# -------------------------

with st.sidebar:

    st.title("🤖 My AI")

    if st.button("➕ New Chat", use_container_width=True):

        st.session_state.messages = []

        st.rerun()

    st.write("Free Online AI")
    st.write("Powered by Gemini")


# -------------------------
# OLD MESSAGES DIKHAO
# -------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# -------------------------
# MESSAGE BOX
# -------------------------

prompt = st.chat_input("Message My AI...")


# -------------------------
# USER SENDS MESSAGE
# -------------------------

if prompt:

    # User message history me save
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # User message screen par dikhao
    with st.chat_message("user"):

        st.markdown(prompt)


    # -------------------------
    # AI RESPONSE
    # -------------------------

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            # Purani conversation Gemini ko bhejne ke liye
            conversation = ""

            for message in st.session_state.messages:

                if message["role"] == "user":

                    conversation += (
                        "User: "
                        + message["content"]
                        + "\n"
                    )

                else:

                    conversation += (
                        "Assistant: "
                        + message["content"]
                        + "\n"
                    )

            conversation += "Assistant:"


            # -------------------------
            # GEMINI API CALL
            # -------------------------

            try:

                interaction = client.interactions.create(
                    model="gemini-3.8-flash",
                    input=conversation
                )

                answer = interaction.output_text

                st.markdown(answer)


            # -------------------------
            # GEMINI ERRORS
            # -------------------------

            except errors.APIError as e:

                if e.code == 429:

                    answer = (
                        "⚠️ Free AI limit abhi reach ho gayi hai.\n\n"
                        "Thodi der baad dobara try karo."
                    )

                elif e.code == 401 or e.code == 403:

                    answer = (
                        "⚠️ AI service authentication problem aa rahi hai."
                    )

                else:

                    answer = (
                        "⚠️ AI service me temporary problem aa gayi hai.\n\n"
                        "Please thodi der baad try karo."
                    )

                st.warning(answer)


            # -------------------------
            # OTHER ERRORS
            # -------------------------

            except Exception:

                answer = (
                    "⚠️ Kuch unexpected error aa gaya.\n\n"
                    "Please thodi der baad try karo."
                )

                st.warning(answer)


    # -------------------------
    # AI ANSWER HISTORY ME SAVE
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )
