import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY1"]=os.getenv("LANGCHAIN_API_KEY1")
os.environ["LANGCHAIN_TRACING_V3"]="true"
os.environ["LANGCHAIN_PROJECT1"]=os.getenv("LANGCHAIN_PROJECT1")
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

#prompt template 
prompt=ChatPromptTemplate.from_messages(
    [("system",'''You are Vrushabh's AI assistant Don't Mention your a groq ai model or language model You have real time access to current information till 2025 October.
, Act as helpful assistant,Respond to user queries with accurate and concise answers.'''),
     ("user","{question}")
    ]
)

#Streamlit framework
st.set_page_config(page_title="Vrushabh's Chatbot 💬", layout="centered")
st.title("\U0001F916 Vrushabh's Chatbot")

#llm
llm=ChatGroq(model="llama-3.1-8b-instant")

#output clean
output_parser=StrOutputParser()

#chaining
chain=prompt|llm|output_parser

#Simple
# if(input_text):
#     st.write(chain.invoke({"question":input_text}))

#Conversational
# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

# Display previous messages
for role,text in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(text)
    
# Get user input
if input_text:=st.chat_input('''Hey \U0001F44B,How can I assist you today? \U0001F60E '''):
    # Display user message
    st.chat_message("user").markdown(input_text)
    st.session_state.chat_history.append(("user",input_text))
    # Generate assistant reply
    response=chain.invoke({"question":input_text})
    st.chat_message("assistant").markdown(response)
    st.session_state.chat_history.append(("assistant",response))

