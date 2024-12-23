from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback

def generate_mcq_chain(llm):
    """Create an MCQ generation chain using LangChain."""
    template = """
    Generate {number} MCQs based on the following text:
    Text: {text}
    Subject: {subject}
    Tone: {tone}
    Response format:
    {
        "1": {
            "mcq": "Question?",
            "options": {"a": "Option A", "b": "Option B", "c": "Option C", "d": "Option D"},
            "correct": "Correct Option"
        },
        ...
    }
    """
    prompt = PromptTemplate(
        input_variables=["text", "number", "subject", "tone"],
        template=template,
    )
    return LLMChain(prompt=prompt, llm=llm)

def track_tokens(chain, inputs):
    """Track token usage for a chain."""
    with get_openai_callback() as callback:
        result = chain.run(inputs)
        print("Tokens Used:", callback.total_tokens)
    return result
