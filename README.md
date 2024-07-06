# ChatGPT Interface

A simple web interface for interacting with the ChatGPT AI model using Flask and Transformers.

## Features

*   User-friendly chat interface for asking questions and receiving responses
*   Supports text-based input and output
*   Toggleable dark mode for a sleeker look
*   Error handling for unexpected errors

## Technical Details

### Backend

*   Built using Flask, a lightweight Python web framework
*   Utilizes the Transformers library for text generation
*   Handles POST requests to the `/ask` endpoint, generating responses based on user input

### Frontend

*   Built using HTML, CSS, and JavaScript (with jQuery)
*   Features a responsive design with a chat log and input field
*   Supports dark mode toggle via a button click

### Code Structure

*   `app.py`: The Flask application code, including the `/ask` endpoint and error handling
*   `index.html`: The HTML template for the chat interface
*   `style.css`: The CSS styles for the chat interface (not included in this repository)
*   `script.js`: The JavaScript code for handling user input, sending requests to the backend, and updating the chat log

## Getting Started

1.  Install the required dependencies: `pip install flask transformers`
2.  Run the application: `python app.py`
3.  Open a web browser and navigate to `http://localhost:5000`
4.  Start chatting with the AI!

## Executed

![](/templates/Screenshot%202024-07-06%20at%2011.54.07 PM.png)

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contributing

Contributions are welcome! If you'd like to improve the interface or add new features, please submit a pull request.

## Acknowledgments

This project was inspired by the ChatGPT model and the Transformers library. Special thanks to the developers and maintainers of these projects!
