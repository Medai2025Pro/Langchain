
##### Blog Generation LLm App

import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import json
from langchain_core.output_parsers import StrOutputParser

# Set page configuration  
st.set_page_config(page_title="Blog Generator", page_icon='🤖', layout='centered')
# Define functions to interact with the JSON file
def load_settings():  
    try:
        with open("settings.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_settings(settings): # settings : The dictionary containing the settings.
    with open("settings.json", "w") as file:
        json.dump(settings, file, indent=4)


# Load settings or use default values if not found
settings = load_settings()

temperature_default = settings.get("temperature", 0.7)
model_default = settings.get("model", "gpt-3.5-turbo")

# Sidebar settings
st.sidebar.header("Settings")

temperature = st.sidebar.slider("***Temperature***", 0.1, 1.0, temperature_default)
model = st.sidebar.selectbox(
    "***Model***",
    ["gpt-3.5-turbo", "gpt-4", "gpt-3.5-turbo-16k","dall-e-3"],
    index=0 if model_default == "gpt-3.5-turbo" else 1,
)

# Update settings with the new values
settings.update(
    {
        "temperature": temperature,
        "model": model,
    }
)
save_settings(settings)

## Function To get response from openai model

def getopenairesponse(input_text,num_words,blog_style,language):

    
    llm=ChatOpenAI(model=model,temperature=temperature)
    outputparser = StrOutputParser()
    ## Prompt Template 

    template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {num_words} words. keep in mind that you must generate the blog with the {language} language
            """
    #Select Audience: Choose the audience type for the blog from the dropdown list labeled "Writing the blog for". The default selection is "Researchers".
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words','language'],
                          template=template)
    
    ## Generate the ressponse from the openai model
    response=outputparser.parse(llm.invoke(prompt.format(blog_style=blog_style,input_text=input_text,num_words=num_words,language=language)))
    return response

def translate_text(text, source_language, target_language):
    llm = ChatOpenAI(model=model, temperature=temperature)
    output_parser = StrOutputParser()
    
    template = """
        Translate the following text from {source_language} to {target_language}: "{text}"
            """
    prompt = PromptTemplate(input_variables=["text", "source_language", "target_language"],
                            template=template)
    
    response = output_parser.parse(llm.invoke(prompt.format(text=text,
                                                             source_language=source_language,
                                                             target_language=target_language)))
    return response.content


st.title("***Generate Blogs v1.0*** 🤖")

input_text=st.text_input("***Enter the Blog Topic(required)***")

## creating to more columns for additonal 2 fields

col1,col2,col3=st.columns([5,5,5])  # The argument [5, 5] specifies the width ratio of the columns, where both columns have equal width.

with col1:
    num_words=st.text_input('***Number of Words (required)***')
with col2:
    blog_style=st.selectbox('***Writing the blog for (required)***',
                            ('Researchers','Data Scientist','Common People'),index=0) ## The index=0 argument sets the default selection to the first option ("Researchers").
with col3:
    language = st.text_input('***Enter the language(required)***')

submit=st.button("*Generate*")

## Final response
# Custom validation
if submit:
    if not input_text or not num_words or not blog_style or not language:
        st.warning("Please fill in all required fields!🤬")
    else:
        response = getopenairesponse(input_text, num_words, blog_style, language)
        translated_success_message = translate_text("Your blog has been generated successfully.", "en", language)
        st.info("### Generated Blog:")
        with st.container():
            num_lines = len(response.content.split('\n'))
            st.markdown(
                f'<div style="border: 3px double  #101010; border-radius: 8px; padding: 10px">{response.content}</div>', 
                unsafe_allow_html=True
            )
        st.success(translated_success_message)
       

