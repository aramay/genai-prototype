# import packages
from dotenv import load_dotenv
from openai import OpenAI
import os
import streamlit as st
# load environment varaiable from .env file
load_dotenv()

client = OpenAI(
    # This is default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Initialize OpenAI client
# client = OpenAI()
st.title("GenAI Protype tool")
st.write("This is first Streamlit app")

@st.cache_data
def get_api_response(user_prompt, temperature):
    response = client.responses.create(
        model="gpt-4o",
        input=[
            {"role": "user", "content": user_prompt} # prompt
        ],
        # temperature: 0.7, # A bit of creativity
        max_output_tokens=100 # Limit response length

    )
    return response
    
user_prompt = st.text_input("Enter your prompt")

temperature = st.slider(
    label="temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1,
    help="Controlls randomness 0 = deterministic, 1 = very creative"
)

with st.spinner("AI is working.."):
    response = get_api_response(user_prompt, temperature)
    st.write(response.output_text)
    print(response.output_text)    

# print the response from OpenAI

