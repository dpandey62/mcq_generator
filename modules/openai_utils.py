import openai
from config import OPENAI_API_KEY

def initialize_openai():
    openai.api_key = OPENAI_API_KEY
