'''
This is the main file for the chatbot application.
It is a simple Flask application that allows users to chat with a chatbot.
The chatbot is based on the Blenderbot model from Facebook.
'''
# Importing the necessary libraries
import json
from flask import Flask, request, render_template
from flask_cors import CORS
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Initializing the Flask application
app = Flask(__name__)
CORS(app)

# Loading the Blenderbot model and tokenizer
MODEL_NAME = "facebook/blenderbot-400M-distill"
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Initializing the conversation history
conversation_history = []

# Defining the route for the chatbot
@app.route('/chatbot', methods=['POST'])
def handle_prompt():
    '''
    This function handles the prompt from the user.
    It gets the prompt from the request and creates a conversation history string.
    It then tokenizes the input text and history and generates the response from the model.
    '''
    # Getting the prompt from the request
    data = request.get_data(as_text=True)
    data = json.loads(data)
    input_text = data['prompt']

    # Create conversation history string
    history = "\n".join(conversation_history)

    # Tokenize the input text and history
    inputs = tokenizer.encode_plus(history, input_text, return_tensors="pt")

    # Generate the response from the model
    outputs = model.generate(**inputs, max_length=60)
    # max_length will cause the model to crash at some point as history grows

    # Decode the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

    # Add interaction to conversation history
    conversation_history.append(input_text)
    conversation_history.append(response)

    return response

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
