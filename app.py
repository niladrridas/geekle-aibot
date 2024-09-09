from flask import Flask, request, jsonify, render_template  # Import necessary modules from Flask
import os  # Import os module for operating system related tasks
from transformers import pipeline  # Import pipeline from transformers for text generation

app = Flask(__name__)  # Initialize the Flask application

@app.route('/')  # Define the route for the home page
def index():
    return render_template('index.html')  # Render the index.html template

@app.route('/ask', methods=['POST'])  # Define the route for the /ask endpoint with POST method
def ask():
    data = request.json  # Get the JSON data from the request
    user_message = data['message']  # Extract the user's message from the JSON data

    try:
        # Initialize the text generation pipeline
        generator = pipeline('text-generation')

        # Generate text based on the user's message
        response = generator(user_message, max_length=150)

        # Extract the generated text from the response
        bot_message = response[0]['generated_text'].strip()

        # Add some basic response formatting
        bot_message = bot_message.capitalize() + '.'

        # Return the generated message as a JSON response
        return jsonify({'message': bot_message})
    except Exception as e:
        # Return an error message as a JSON response if an exception occurs
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode