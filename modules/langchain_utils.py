from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

def create_chain():
    """Creates and returns an LLMChain for MCQ generation."""
    template = """
    Create {number} multiple-choice questions from the following text:
    Text: {text}
    Subject: {subject}
    Tone: {tone}
    
    Response format:
    {
        "1": {
            "mcq": "Question text here",
            "options": {
                "a": "Option A",
                "b": "Option B",
                "c": "Option C",
                "d": "Option D"
            },
            "correct": "Correct answer text"
        }
    }
    """
    prompt = PromptTemplate(input_variables=["text", "number", "tone", "subject"], template=template)
    llm = ChatOpenAI(temperature=0.7)
    return LLMChain(llm=llm, prompt=prompt)
