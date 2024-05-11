# End To End LLM Project Using LLAMA 2- Open Source LLM Model From Meta
### This code creates a simple Streamlit web app for generating blog content using the LLAMA 2 model

##### Blog Generation LLm App

import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms.ctransformers import CTransformers

## Function To get response from LLAma 2 model

def getLLamaresponse(input_text,num_words,blog_style):

    ### LLama2 model
    ## CTransformers: A class for working with LLAMA 2, an open-source LLM model from Meta
    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})
    
    ## Prompt Template 

    template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {num_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,num_words=num_words))
    return response






st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the Blog Topic")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    num_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','Common People'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
    st.write(getLLamaresponse(input_text,num_words,blog_style))


# Explanation full code : 

"""

Sure, let's break down the code step by step:

Imports:

streamlit: Streamlit library for creating interactive web apps.
PromptTemplate: A template for generating prompts.
CTransformers: A class for working with LLAMA 2, an open-source LLM model from Meta.
Function Definition (getLLamaresponse):

This function takes three parameters: input_text, no_words, and blog_style.
Inside the function:
It initializes the LLAMA 2 model using CTransformers with specific configurations.
It defines a prompt template using PromptTemplate.
It generates a response from the LLAMA 2 model using the provided inputs and the prompt template.
Finally, it returns the response.
Setting Page Configuration:

Sets the page configuration for the Streamlit app.
Header:

Displays a header for the Streamlit app titled "Generate Blogs".
User Input:

Provides a text input field for the user to enter the blog topic.
Creates two columns for additional input fields: one for the number of words and another for selecting the target audience (blog style).
Submit Button:

Displays a button labeled "Generate" for submitting the user inputs.
Final Response:

When the "Generate" button is clicked (submit is True), the getLLamaresponse function is called with the user inputs.
The generated response is displayed on the app.
Overall, this code creates a simple Streamlit web app for generating blog content using the LLAMA 2 model. Users can input the topic, the number of words, and select the target audience, and the app generates a blog post accordingly using the LLAMA 2 model.

"""
















































