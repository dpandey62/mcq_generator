import unittest
from modules.mcq_generator import generate_mcqs

class TestMCQGenerator(unittest.TestCase):
    def test_mcq_output(self):
        text = "Water is essential for life. Its chemical formula is H2O."
        subject = "Science"
        tone = "Neutral"
        number = 2
        llm = None  # Mock or actual LLM instance
        mcqs = generate_mcqs(text, number, subject, tone, llm)
        self.assertIn("1", mcqs)
        self.assertIn("mcq", mcqs["1"])
