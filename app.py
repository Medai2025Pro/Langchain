#  End To End LLM Conversational Q&A Chatbot With Deployment.

## Conversational Q&A Chatbot
import streamlit as st

from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()
## Streamlit UI
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat Bro 😂")

chat=ChatOpenAI(temperature=0.6)

# "flowmessages" is indeed a list. In the provided code snippet, flowmessages is used to store the messages exchanged during the conversation between the user and the chatbot.
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="Your are a comedian AI assitant")
    ]

## Function to load OpenAI model and get respones

def get_chatmodel_response(question):
    
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat.invoke(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input=st.text_input("Input: ",key="input")
response=output_parser.parse(get_chatmodel_response(input))

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("""
                 
                 😎😎😎
                 
                 
                 """ )
    
    st.write("***" + response + "***")






















