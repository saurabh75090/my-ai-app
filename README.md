# 🤖 My AI – Online AI Chatbot

## 📌 Project Overview

**My AI** is a ChatGPT-style online AI chatbot application built using **Python, Streamlit, and the Google Gemini API**.

The application allows users to open a web link, type a question, and receive an AI-generated response.

The final application is deployed online, so users do not need to install Python, VS Code, Ollama, or any development tools.

Users only need:

- A web browser
- An internet connection
- The application link

---

## 🌐 Live Application

You can access the application here:

https://my-ai-app-dayxqlsgqsjzsaydawvzue.streamlit.app/

---

# 🎯 Project Goal

The goal of this project was to understand how an AI chatbot application works from beginning to deployment.

The basic flow of the application is:

```text
User
  ↓
Streamlit Web Application
  ↓
Python
  ↓
Gemini API
  ↓
Gemini AI Model
  ↓
Generated Response
  ↓
Displayed to User
```

The application also supports follow-up questions by keeping the current conversation in session memory.

---

# 🛠 Technologies Used

## Python

Python is the main programming language used to build the application logic.

## Streamlit

Streamlit is used to create the web interface and the ChatGPT-style messaging system.

## Google Gemini API

The Gemini API provides the AI model that generates answers to user questions.

## Google GenAI Python SDK

The Google GenAI Python library is used to connect the Python application with Gemini.

## GitHub

GitHub is used to store and manage the project source code.

## Streamlit Community Cloud

Streamlit Community Cloud is used to host the application online and provide a public web link.

---

# 🚀 Development Process

## 1. Installing Python

The first step was installing Python on Windows.

The installation was checked using:

```bash
python --version
```

This confirmed that Python was installed correctly.

---

## 2. Installing Visual Studio Code

Visual Studio Code was installed and used as the main code editor.

The Microsoft Python extension was also installed to make Python development easier.

A project folder was created:

```text
MY AI APP
```

The main application file was created inside the folder:

```text
app.py
```

---

## 3. Testing Python

Before building the AI application, a simple Python program was tested:

```python
print("Hello Saurabh")
```

The program was executed using:

```bash
python test.py
```

This confirmed that Python and VS Code were working properly.

---

# 📦 4. Creating a Virtual Environment

A Python virtual environment was created using:

```bash
python -m venv .venv
```

A virtual environment keeps the libraries required by one project separate from other Python projects.

The environment folder was:

```text
.venv
```

---

# 🌐 5. Installing Streamlit

Streamlit was installed using:

```bash
python -m pip install streamlit
```

The installation was tested using:

```bash
python -m streamlit hello
```

Streamlit opened a demo application in the web browser.

The local Streamlit address was similar to:

```text
http://localhost:8501
```

This means the application was initially running only on the local computer.

---

# 🧪 6. Creating the First Web Application

The first version of the application was very simple.

Example:

```python
import streamlit as st

st.title("My First AI App")

question = st.text_input("Ask me something:")

if st.button("Send"):
    st.write("You asked:", question)
```

At this stage, the application did not contain AI.

It only:

```text
Accepted a question
        ↓
Stored the question
        ↓
Displayed the same question
```

---

# 💬 7. Creating a ChatGPT-Style Interface

The normal text input was later replaced with Streamlit's chat interface.

A ChatGPT-style message input was created using:

```python
st.chat_input("Message My AI...")
```

User messages were displayed using:

```python
st.chat_message("user")
```

AI messages were displayed using:

```python
st.chat_message("assistant")
```

This created a much more natural chatbot interface.

---

# 🧠 8. Adding Conversation Memory

Streamlit Session State was used to store the current conversation.

Example:

```python
st.session_state.messages
```

Messages are stored in a structure similar to:

```python
{
    "role": "user",
    "content": "What is VLAN?"
}
```

AI messages are stored like:

```python
{
    "role": "assistant",
    "content": "VLAN stands for Virtual Local Area Network..."
}
```

This allows conversations like:

```text
User:
What is VLAN?

AI:
VLAN stands for Virtual Local Area Network...

User:
Give me a real-life example.

AI:
A real-life example would be...
```

The AI receives the previous conversation and can understand follow-up questions.

The current version uses temporary session memory.

It does not currently use a permanent database for saved conversations.

---

# ➕ 9. Adding a New Chat Button

A **New Chat** button was added to the sidebar.

Example:

```python
if st.button("➕ New Chat"):
    st.session_state.messages = []
    st.rerun()
```

When the button is pressed, the current conversation is cleared.

---

# 🖥 10. Testing a Local AI Model

The first AI version used **Ollama** and a small **Qwen AI model**.

The architecture was:

```text
User
 ↓
Streamlit
 ↓
Python
 ↓
Ollama
 ↓
Qwen AI Model
 ↓
Response
```

This version worked locally without using a paid AI API.

However, it had one important problem.

If the application was given to another person, they would also need:

```text
Ollama
AI Model
Local Setup
```

Because the goal was to create an application that anyone could open directly, the local AI approach was replaced with an online AI API.

---

# 🌐 11. Connecting Google Gemini

The application was later connected to the Google Gemini API.

The required Python package was installed using:

```bash
python -m pip install -U google-genai
```

The Gemini library was imported using:

```python
from google import genai
```

A Gemini client was created using:

```python
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)
```

The application sends the user's conversation to Gemini.

Gemini generates an answer.

The answer is then displayed inside the Streamlit chat interface.

The final flow became:

```text
User Question
      ↓
Streamlit App
      ↓
Python
      ↓
Gemini API
      ↓
Gemini AI
      ↓
AI Response
      ↓
Streamlit App
      ↓
User
```

---

# 🔐 12. Securing the API Key

The Gemini API key is a secret credential.

It was not written directly inside `app.py`.

For local development, the key was stored inside:

```text
.streamlit/
└── secrets.toml
```

The file contains:

```toml
GEMINI_API_KEY = "YOUR_SECRET_API_KEY"
```

The application accesses the key using:

```python
st.secrets["GEMINI_API_KEY"]
```

This prevents the secret key from being written directly into the application source code.

---

# 🛡 13. Creating `.gitignore`

A `.gitignore` file was created so private and unnecessary files would not be uploaded to GitHub.

The file contains:

```text
.venv/
.streamlit/secrets.toml
__pycache__/
```

This prevents the following from being uploaded:

```text
Virtual Environment
API Key
Python Cache Files
```

The API key should never be uploaded to a public GitHub repository.

---

# 📋 14. Creating `requirements.txt`

A `requirements.txt` file was created.

It contains:

```text
streamlit
google-genai
```

This file tells the cloud server which Python libraries must be installed before running the application.

---

# 🐙 15. Uploading the Project to GitHub

A GitHub repository was created:

```text
my-ai-app
```

The main project files were uploaded.

The repository structure is similar to:

```text
my-ai-app/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

The following private files were not uploaded:

```text
.venv/
.streamlit/secrets.toml
```

---

# ☁️ 16. Deploying the Application

The GitHub repository was connected to **Streamlit Community Cloud**.

Deployment settings used:

```text
Repository:
my-ai-app

Branch:
main

Main File:
app.py
```

The Gemini API key was added separately inside the Streamlit Cloud Secrets settings.

Example:

```toml
GEMINI_API_KEY = "SECRET_API_KEY"
```

After deployment, Streamlit generated a public web address for the application.

---

# 🔗 17. Public Application Link

The deployed application is available at:

https://my-ai-app-dayxqlsgqsjzsaydawvzue.streamlit.app/

Anyone with the link can open the application using a web browser.

---

# 🏗 Final Application Architecture

The final application works like this:

```text
User's Phone / Laptop
        ↓
Web Browser
        ↓
Public Streamlit URL
        ↓
Streamlit Community Cloud
        ↓
Python app.py
        ↓
Google Gemini API
        ↓
Gemini AI Model
        ↓
Generated Response
        ↓
Streamlit Interface
        ↓
User
```

---

# 👤 Final User Experience

The user only needs to:

```text
Open Browser
     ↓
Open My AI Link
     ↓
Type Question
     ↓
Send Message
     ↓
Receive AI Answer
```

The final user does NOT need:

```text
Python ❌
VS Code ❌
Terminal ❌
Virtual Environment ❌
Ollama ❌
AI Model Download ❌
GitHub ❌
```

The user only needs:

```text
Internet Connection ✅
Web Browser ✅
Application Link ✅
```

---

# 📊 Gemini Free Tier Limits

The project currently uses the Gemini API Free Tier.

During testing, the project's Gemini rate-limit dashboard showed approximately:

```text
RPM = 5 requests per minute

TPM = 250,000 input tokens per minute

RPD = 20 requests per day
```

During testing, the daily usage reached:

```text
23 / 20 requests
```

This caused a rate-limit error.

The exact limits can change depending on the Gemini model, Google project, account, and Google's current policies.

---

# ⚠️ Rate Limit Error

When the free API quota was exceeded, the application originally displayed a technical error such as:

```text
RateLimitError
Error Code: 429
```

This was not a good experience for normal users.

---

# 🚨 18. Adding Error Handling

Error handling was added to the application.

The Gemini API call was placed inside a `try` block.

Example:

```python
try:

    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=conversation
    )

    answer = interaction.output_text

except errors.APIError as e:

    if e.code == 429:

        answer = (
            "⚠️ Free AI limit has been reached. "
            "Please try again later."
        )
```

Now, instead of displaying a large technical traceback, the application can show a simple message:

```text
⚠️ Free AI limit has been reached.

Please try again later.
```

This makes the application easier for normal users to understand.

---

# 💾 Chat Data

The application currently uses:

```python
st.session_state
```

for chat history.

This means the current conversation is stored temporarily during the active session.

The application currently does not have a separate permanent chat-history database.

If permanent chat history is required in the future, a database can be added.

Examples include:

```text
SQLite
PostgreSQL
Firebase
Supabase
```

---

# ✅ Current Features

The current application includes:

- ChatGPT-style AI chat interface
- Google Gemini AI integration
- Online access
- Public application URL
- User and AI chat messages
- Follow-up question support
- Temporary conversation memory
- New Chat button
- Sidebar
- Gemini API integration
- Secure API key management
- `.gitignore`
- `requirements.txt`
- GitHub repository
- Streamlit Cloud deployment
- API rate-limit handling
- User-friendly error messages
- Desktop browser support
- Mobile browser support

---

# 📚 What I Learned From This Project

This project helped me understand the basics of:

- Python programming
- VS Code
- Python files
- Python packages
- `pip`
- Virtual environments
- Streamlit
- Web application development
- Chat interfaces
- Session state
- AI models
- AI APIs
- Google Gemini API
- API keys
- Secret management
- API rate limits
- Error handling
- GitHub
- GitHub repositories
- `.gitignore`
- `requirements.txt`
- Cloud deployment
- Streamlit Community Cloud
- Public web applications
- Local AI vs Cloud AI

---

# 🔄 Local AI vs Online AI

## Local AI Version

The first version used:

```text
Python
↓
Streamlit
↓
Ollama
↓
Qwen Model
```

Advantages:

- No API cost for local inference
- AI runs on the local computer

Disadvantages:

- Ollama must be installed
- AI model must be downloaded
- Uses local RAM and CPU
- Difficult to share with other users

---

## Online AI Version

The final version uses:

```text
Python
↓
Streamlit
↓
Gemini API
↓
Gemini AI
```

Advantages:

- No AI model installation for users
- Easy to share
- Works on phones and computers
- User only needs a web browser
- AI processing happens through the online API

Disadvantages:

- Requires internet
- Free API has usage limits

For this project, the online API approach was more suitable because the application needed to be easily shareable.

---

# 🔮 Future Improvements

The project can be improved further by adding:

## Permanent Chat History

Store conversations permanently in a database.

## Multiple Chats

Allow users to create and switch between multiple conversations like ChatGPT.

## User Accounts

Add login and signup functionality.

## Better User Interface

Improve colors, layout, sidebar, buttons, and animations.

## Streaming Responses

Display AI responses word-by-word instead of waiting for the entire answer.

## File Upload

Allow users to upload files.

## PDF Question Answering

Allow users to upload PDFs and ask questions about them.

## Image Understanding

Allow users to upload images and ask AI questions about them.

## Voice Input

Allow users to speak instead of typing.

## Voice Output

Allow the AI to speak its answers.

## Internet Search

Allow the AI to retrieve current information from the web.

## Database Integration

Use a database for permanent user and chat storage.

## Android Application

Create an Android version of My AI.

## Windows Desktop Application

Create a Windows desktop version.

## Custom Domain

Connect the application to a custom website domain.

---

# 📁 Final Project Structure

```text
my-ai-app/
│
├── app.py
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

Local-only files:

```text
MY AI APP/
│
├── .venv/
│
├── .streamlit/
│   └── secrets.toml
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📝 Summary

This project started as a basic Python program and gradually became a complete online AI chatbot.

The development process included:

```text
Python Installation
        ↓
VS Code Setup
        ↓
First Python Program
        ↓
Virtual Environment
        ↓
Streamlit Installation
        ↓
Basic Web Application
        ↓
Chat Interface
        ↓
Local Ollama AI
        ↓
Gemini API
        ↓
Conversation Memory
        ↓
API Key Security
        ↓
GitHub
        ↓
Streamlit Cloud
        ↓
Public AI Application
        ↓
Error Handling
```

The final result is a shareable AI chatbot that can be opened directly from a web browser without requiring the user to install Python or any development tools.

---

# 👨‍💻 Project

**Project Name:** My AI

**Project Type:** AI Chatbot Web Application

**Programming Language:** Python

**Web Framework:** Streamlit

**AI Backend:** Google Gemini API

**Source Code Hosting:** GitHub

**Deployment:** Streamlit Community Cloud

**Live Application:**

https://my-ai-app-dayxqlsgqsjzsaydawvzue.streamlit.app/
