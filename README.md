# NextGenAI: Flask Application on Vercel

This project is a Flask application that serves an `index.html` file from the root directory and uses the Hugging Face Transformers library for text generation.

## Project Structure

```
my-flask-app/
├── index.py
├── index.html
└── requirements.txt
```

## `index.py` (Flask Application)

```python
from flask import Flask, request, jsonify, send_from_directory
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
```

## `requirements.txt`

```
Flask
transformers
torch
```

## `vercel.json`

Create a `vercel.json` file with the following content:

```json
{
  "version": 2,
  "builds": [
    { "src": "index.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "index.py" }
  ]
}
```

## Deployment Steps

1. **Install Vercel CLI**:

    ```sh
    npm install -g vercel
    ```

2. **Log in to Vercel**:

    ```sh
    vercel login
    ```

3. **Deploy Your App**:

    Navigate to the root of your project directory and run:

    ```sh
    vercel
    ```

    Follow the prompts provided by Vercel to complete the deployment.

After these steps, your Flask application should be deployed to Vercel, and it will serve the `index.html` file from the root directory. If you encounter any errors, check the Vercel logs for more details.