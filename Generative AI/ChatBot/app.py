from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true' 

##prompt Templet

prompt = ChatPromptTemplate(
        [
                ('system','You are a helpful assistant. Please response to the user queries'),
                ('user','Question:{question}')
        ]
)
#Streamlit Framework

st.title('Langchain Demo with Ollama')
input_text = st.text_input('Search the topic you want')

##Ollama gemma:2b Model

llm = Ollama(model = 'gemma:2b')
output_preser = StrOutputParser()
chain = prompt|llm|output_preser

if input_text:
        st.write(chain.invoke({'question':input_text}))