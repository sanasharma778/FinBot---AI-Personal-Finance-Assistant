# This file is the brain of our chatbot
# It handles connecting to the AI model and getting responses

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# This line reads the .env file and loads our API key
load_dotenv()

def get_model():
    """This function creates and returns our AI model"""
    return ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant"
    )

def get_chat_response(chat_model, messages, system_prompt):
    """This function sends messages to the AI and gets a response back"""
    
    try:
        # Start with the system prompt — this tells AI how to behave
        formatted_messages = [SystemMessage(content=system_prompt)]
        
        # Add the full conversation history
        for msg in messages:
            if msg["role"] == "user":
                formatted_messages.append(HumanMessage(content=msg["content"]))
            else:
                formatted_messages.append(AIMessage(content=msg["content"]))
        
        # Send everything to Groq and get response
        response = chat_model.invoke(formatted_messages)
        
        # Return just the text content
        return response.content
    
    except Exception as e:
        return f"Error: {str(e)}"