from langchain_utils import generate_mcq_chain, track_tokens

def generate_mcqs(text, number, subject, tone, llm):
    """Generate MCQs based on input parameters."""
    chain = generate_mcq_chain(llm)
    inputs = {"text": text, "number": number, "subject": subject, "tone": tone}
    mcqs = track_tokens(chain, inputs)
    return mcqs
