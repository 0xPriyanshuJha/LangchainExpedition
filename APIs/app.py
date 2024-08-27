from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()


openai_api_key = os.getenv('OPENAI_API_KEY')
langchain_api_key = os.getenv('LANGCHAIN_API_KEY')

if not openai_api_key or not langchain_api_key:
    raise ValueError("API keys for OpenAI and LangChain must be set in the environment.")

os.environ['OPENAI_API_KEY'] = openai_api_key
os.environ['LANGCHAIN_API_KEY'] = langchain_api_key
os.environ['LANGCHAIN_TRACING_V2'] = "true"

app = FastAPI(
    title="Langchain API",
    description="API for Langchain",
    version="1.0"
)

add_routes(
    app,
    ChatOpenAI(),
    path = "/openai"
)

# OpenAI model
model = ChatOpenAI()

# ollama model
llm = Ollama(model="llama2")

# prompt1 interacting with chatopenAI
prompt1 = ChatPromptTemplate.from_template("Write me an essay about some {topic} with 100 words")
# prompt2 interacting with opensource AI
prompt2 = ChatPromptTemplate.from_template("Write me an poem about some {topic} with 100 words")

add_routes(
    app,
    prompt1|model,
    path = "/essay"
)

add_routes(
    app,
    prompt2|llm,
    path = "/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)