from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

#Chat Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assitant. Please respond to the user's queries."),
        ("user", "Question:{question}")
    ]
)

# Streamlit
st.title("Langchain Expedition")
input_text = st.text_area("Search anything you want!")

#openAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()