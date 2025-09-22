import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm=Ollama(model="gemma:2b")

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

#prompt setup
prompt=ChatPromptTemplate([
    ("system","You are helpful and intelligent assistant. Asnwer the questions asked"),
    ("user","Question:{question}")
])

st.title("Langchain: LLM Gemma2b")
input_text=st.text_input("Whats on your mind?")

parser=StrOutputParser()
chain=prompt|llm|parser

if input_text:
    st.write(chain.invoke({"question":input_text}))