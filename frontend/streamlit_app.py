# frontend/streamlit_app.py
# This is the UI of our chatbot — everything the user sees and interacts with

import streamlit as st
import sys
import os

# This tells Python where to find our app folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import our own files
from app.chatbot import get_model, get_chat_response
from app.prompts import SYSTEM_PROMPTS

# ---- PAGE CONFIGURATION ----
st.set_page_config(
    page_title="FinBot — Personal Finance Assistant",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- SIDEBAR ----
with st.sidebar:
    st.title("💰 FinBot")
    st.caption("Your Personal Finance Assistant")
    
    st.divider()
    
    # Mode selector — this switches the system prompt
    st.subheader("Choose Your Mode")
    selected_mode = st.selectbox(
        "What do you need help with?",
        options=list(SYSTEM_PROMPTS.keys())
    )
    
    st.divider()
    
    # Show what each mode does
    st.caption("💰 Budget Advisor — plan your monthly budget")
    st.caption("📈 Investment Basics — learn about investing")
    st.caption("🏦 Saving Goals — set and reach saving targets")
    st.caption("🇬🇧 UK Finance Guide — UK specific finance help")
    
    st.divider()
    
    # Clear chat button
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    # Download chat button
    if "messages" in st.session_state and st.session_state.messages:
        chat_text = f"FinBot Chat Export — {selected_mode}\n"
        chat_text += "=" * 40 + "\n\n"
        for msg in st.session_state.messages:
            role = "You" if msg["role"] == "user" else "FinBot"
            chat_text += f"{role}:\n{msg['content']}\n\n"
        
        st.download_button(
            label="📥 Download Chat",
            data=chat_text,
            file_name="finbot_chat.txt",
            mime="text/plain",
            use_container_width=True
        )

# ---- MAIN PAGE ----
st.title(f"💰 FinBot — {selected_mode}")
st.caption("Ask me anything about personal finance. I'm here to help!")

st.divider()

# ---- INITIALISE CHAT HISTORY ----
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---- INITIALISE MODEL ----
if "model" not in st.session_state:
    st.session_state.model = get_model()

# ---- DISPLAY CHAT HISTORY ----
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---- SHOW WELCOME MESSAGE IF CHAT IS EMPTY ----
if not st.session_state.messages:
    with st.chat_message("assistant"):
        st.markdown(f"👋 Hello! I'm FinBot, your personal finance assistant. You're currently in **{selected_mode}** mode. What would you like to know?")

# ---- CHAT INPUT ----
if prompt := st.chat_input("Ask me about budgeting, saving, investing..."):
    
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get and display bot response
    with st.chat_message("assistant"):
        with st.spinner("FinBot is thinking..."):
            system_prompt = SYSTEM_PROMPTS[selected_mode]
            response = get_chat_response(
                st.session_state.model,
                st.session_state.messages,
                system_prompt
            )
            st.markdown(response)
    
    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": response})