from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# Set environment variables
langchain_api_key = os.getenv('LANGCHAIN_API_KEY')

if not  langchain_api_key:
    raise ValueError("API keys for LangChain must be set in the environment.")

os.environ['LANGCHAIN_API_KEY'] = langchain_api_key
os.environ['LANGCHAIN_TRACING_V2'] = "true"


# Chat Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's queries."),
        ("user", "Question:{question}")
    ]
)

# Streamlit
st.title("Langchain with Ollama")
input_text = st.text_area("Search anything you want!")

# Ollama LLM
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Handle input and display output
if input_text:
    try:
        result = chain.invoke({"question": input_text})
        st.write(result)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
