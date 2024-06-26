from flask import Flask, request, jsonify, render_template, send_from_directory
import os
from transformers import pipeline

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_message = data['message']

    try:
        # Initialize the text generation pipeline
        generator = pipeline('text-generation')

        # Generate text
        response = generator(user_message, max_length=150)

        # Extract the generated text
        bot_message = response[0]['generated_text'].strip()

        return jsonify({'message': bot_message})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
