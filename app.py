'''
This is a simple Flask application that serves as a chatbot interface.
It uses the Hugging Face API to get responses from DeepSeek-V3 model.
'''
# Importing the necessary libraries
import os
import json
import requests
from dotenv import load_dotenv
from flask import Flask, request, render_template
from flask_cors import CORS

# Initializing the Flask application
app = Flask(__name__)
CORS(app)

# Setting the API token and URL for the Hugging Face model
load_dotenv() # Load environment variables from .env file
API_URL = "https://router.huggingface.co/fireworks-ai/inference/v1/chat/completions"
# Setting the headers for the API request
headers = {
    "Authorization": f"Bearer {os.getenv('API_TOKEN')}" # API token from environment variable
}

# Defining the route for the chatbot
@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    '''
    This function handles the POST request from the chatbot interface.
    It sends the prompt to the Hugging Face API and returns the response.
    '''
    # Getting the prompt from the request
    data = request.get_data(as_text=True)
    payload = json.loads(data)

    # Setting the model and messages for the API request
    response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
    response = response.json()

    if response.status_code != 200:
        # If the response is not successful, return an error message
        return "Error: Unable to get a response from the model. Please try again later, check your code or your API token."
    # If the response is successful, return the model's response
    return response['choices'][0]['message']['content']

@app.route('/')
def home():
    '''
    This function renders the home page.
    '''
    # Rendering the home page
    return render_template('index.html')

# Running the application
if __name__ == '__main__':
    app.run(debug=False)
