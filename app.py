import streamlit as st
from modules.openai_utils import initialize_openai
from modules.chain_utils import create_chain
from modules.mcq_utils import display_mcq

# Initialize OpenAI API
initialize_openai()

# Streamlit App
st.title("Automated MCQ Generator")

text = st.text_area("Enter the source text for MCQ generation:")
number_of_questions = st.number_input("Number of questions to generate:", min_value=1, max_value=10, step=1)
tone = st.selectbox("Select the tone of questions:", ["Formal", "Informal", "Neutral"])
subject = st.text_input("Enter the subject of the content:")

if st.button("Generate MCQs"):
    if text.strip():
        chain = create_chain()
        response = chain.run({"text": text, "number": number_of_questions, "tone": tone, "subject": subject})
        display_mcq(response)
    else:
        st.error("Please enter some text for MCQ generation.")
