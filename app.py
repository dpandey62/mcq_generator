import streamlit as st
from modules.openai_utils import initialize_openai
from modules.mcq_generator import generate_mcqs

# Initialize API
st.title("AI-Powered MCQ Generator")
api_key = st.text_input("Enter OpenAI API Key:", type="password")
llm = None

if api_key:
    llm = initialize_openai(api_key)
    st.success("OpenAI API Initialized!")

# Input Section
text = st.text_area("Enter the text for MCQ generation:")
subject = st.text_input("Enter the subject:")
tone = st.selectbox("Select the tone:", ["Neutral", "Formal", "Conversational"])
number = st.number_input("Number of MCQs:", min_value=1, max_value=10, value=3)

if st.button("Generate MCQs") and llm:
    mcqs = generate_mcqs(text, number, subject, tone, llm)
    st.json(mcqs)
