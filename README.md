# mcq_generator
This project demonstrates an end-to-end Multiple Choice Question (MCQ) Generator using OpenAI, LangChain, and Streamlit. The application takes input text, generates multiple-choice questions based on the content, and displays the results interactively.

# 🎯 Features

📂 File Upload: Users can upload PDF or text files containing the input text for MCQ generation.

🎛️ Customization: Specify the number of MCQs, subject, and complexity level of questions.

🧠 Intelligent Generation: Leverages the Langchain library and OpenAI API for advanced natural language processing.

📊 Review Generated MCQs: View the generated MCQs in a table format along with a review in the Streamlit app.

📝 Logging: Application events are logged for easy tracking and debugging.

# Techology use
 openai ,
 openai Api Key,
langchain ,
streamlit
# 


# Installation
Clone the repository:https://github.com/dpandey62/mcq_generator



cd mcqgen

Create a virtual environment (optional but recommended):


# Install the required dependencies:

pip install -r requirements.txt

# Set up the API key:

Obtain an API key from OpenAI.

Create a .env file in the project root directory.

Add the following line to the .env file:

OPENAI_API_KEY=your_api_key_here
