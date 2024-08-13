![Ss](https://github.com/niladrridas/geekle-aibot/blob/main/data/ss-tag-bank.png)

# Banking Interface

A sleek web interface for interacting with an AI model using Flask and Transformers. This application provides a user-friendly chat experience with support for dark mode and robust error handling.

## Features

- Interactive chat interface for conversing with an AI model
- Supports text-based input and output
- Toggleable dark mode for enhanced readability
- Error handling for better user experience

## Technical Details

### Backend

- **Framework**: Flask, a lightweight Python web framework
- **AI Model**: Uses the Transformers library to generate text
- **Endpoint**: Handles POST requests at the `/ask` endpoint to generate responses based on user input

### Frontend

- **Technologies**: HTML, CSS, and JavaScript (with jQuery)
- **Design**: Responsive design with a chat log and input field
- **Dark Mode**: Toggle between light and dark themes with a button

### Code Structure

- `app.py`: Contains the Flask application logic, including the `/ask` endpoint and error handling
- `templates/index.html`: HTML template for the chat interface
- `static/style.css`: CSS styles for the chat interface
- `static/script.js`: JavaScript for handling user input, sending requests to the backend, and updating the chat log

## Getting Started

1. Install the required dependencies:
   ```bash
   pip install flask transformers
   ```
2. Run the application:
   ```bash
   python app.py
   ```
3. Open a web browser and navigate to `http://localhost:5000`
4. Start interacting with the AI!

## Requirements

- Python 3.7 or later
- Flask: `pip install flask`
- Transformers: `pip install transformers`

## License

This project is licensed under the MIT License. See `LICENSE` for details.

## Contributing

Contributions are welcome! If you want to enhance the interface or add features, please submit a pull request.
