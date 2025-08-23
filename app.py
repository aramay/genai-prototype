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

response = client.responses.create(
    model="gpt-4o",
    input=[
        {"role": "user", "content": "Explain generative AI in one sentence."} # prompt
    ],
    # temperature: 0.7, # A bit of creativity
    max_output_tokens=100 # Limit response length

)

# print the response from OpenAI
print(response.output_text)
st.write(response.output_text)