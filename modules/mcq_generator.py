import streamlit as st
import json

def display_mcq(response_json):
    """Displays MCQs on the Streamlit app."""
    try:
        mcq_data = json.loads(response_json)
        for q_no, question_data in mcq_data.items():
            st.subheader(f"Q{q_no}: {question_data['mcq']}")
            for option, value in question_data["options"].items():
                st.write(f"{option.upper()}: {value}")
            st.success(f"Correct Answer: {question_data['correct']}")
    except json.JSONDecodeError:
        st.error("Invalid response format from the AI model.")
