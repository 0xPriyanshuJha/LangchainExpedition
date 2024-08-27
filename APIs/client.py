import requests
import streamlit as st

def get_open_ai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
    json={'input': {'topic': input_text}})
    
    if response.status_code == 200:
        try:
            return response.json()['output']['content']
        except ValueError:
            return "Error: Received unexpected response format from server."
    else:
        return f"Error: Server returned status code {response.status_code} with message: {response.text}"

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
    json={'input': {'topic': input_text}})
    
    if response.status_code == 200:
        try:
            return response.json()['output']
        except ValueError:
            return "Error: Received unexpected response format from server."
    else:
        return f"Error: Server returned status code {response.status_code} with message: {response.text}"

st.title("Langchain with LLAMA2 API")
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_open_ai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))
