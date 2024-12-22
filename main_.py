import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
from data import PROMPT

# Load environment variables
load_dotenv()

# Initialize OpenAI client
XAI_API_KEY = os.getenv("XAI_API_KEY")
client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)


# Streamlit UI
st.title("Code Kshetra 2.0 Chatbot")
st.write("Ask me anything about Code Kshetra 2.0! If I can't answer, I'll guide you to the organizers for more help.")

# Input field for user query
user_query = st.text_input("Your Question:", placeholder="Type your question here...")

# Button to submit the query
if st.button("Submit"):
    if user_query.strip():
        try:
            # Query the OpenAI client
            completion = client.chat.completions.create(
                model="grok-2-1212",
                messages=[
                    {"role": "system", "content": PROMPT},
                    {"role": "user", "content": user_query},
                ],
            )

            # Get the chatbot's response
            response = completion.choices[0].message.content.strip()

            # Display the response
            st.success(response)

        except Exception as e:
            # Handle errors
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question before submitting.")
