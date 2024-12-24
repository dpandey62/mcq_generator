import openai
from langchain.llms import OpenAI

def initialize_openai(api_key):
    """Initialize OpenAI API."""
    openai.api_key = OPENAI_KEY
    return OpenAI(model_name="text-davinci-003", temperature=0.7)

def generate_completion(prompt, max_tokens=150):
    """Generate a completion using OpenAI."""
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()
