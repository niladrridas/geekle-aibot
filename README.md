# ✨ Banking Interface – A Premium AI-Powered Chat Experience ✨

Experience the future of AI-powered banking with a sleek, intuitive web interface built using **Flask** and **Transformers**. Interact with cutting-edge AI in real-time, enjoy a beautifully designed chat interface, and toggle between light and dark modes with ease. Designed for clarity, performance, and reliability, this interface ensures a smooth user experience.

## 🔥 Key Features

- 💬 **Interactive Chat**: Engage with an AI model in a seamless, real-time conversation.
- 🌙 **Dark Mode**: Switch between light and dark themes effortlessly for a customizable experience.
- 🚀 **Robust Error Handling**: Experience smoother interactions with enhanced error recovery mechanisms.
- 🖥️ **Sleek Design**: A clean, modern interface built for clarity and ease of use.

## 📸 Visual Highlights

_Hackathon Visuals_

![Event](/data/event.png)
![Visual](/data/visual.png)

## 💻 Technical Breakdown

### 🧠 Backend

- **Framework**: Flask, a powerful yet lightweight Python framework.
- **AI Model**: Leveraging the **Transformers** library for intelligent, context-aware responses.
- **API Endpoint**: Send and receive user inputs at the `/ask` endpoint, delivering fast and accurate AI responses.

### 🎨 Frontend

- **Technologies**: Built with HTML, CSS, and JavaScript (including jQuery).
- **Design**: Responsive chat interface, optimized for both desktop and mobile.
- **Dark Mode**: One-click toggle between light and dark themes for better user experience.

## 🚀 Project Roadmap

1. **Project Setup**
   - Install necessary libraries: Flask, transformers.
   - Initialize a Flask application.

2. **Create Routes**
   - Define a home route to render the main page.
   - Define an `/ask` route to handle POST requests for generating responses.

3. **Implement Text Generation**
   - Use Hugging Face's `pipeline` for text generation.
   - Process user input and generate a response using the text generation model.

4. **Error Handling**
   - Implement error handling to manage exceptions during text generation.

5. **Testing and Debugging**
   - Test the application to ensure it generates appropriate responses.
   - Debug any issues that arise during testing.

6. **Deployment**
   - Deploy the Flask application to a web server or cloud platform.

### 🏗️ Code Architecture

- **`app.py`**: The core of the Flask application, managing AI interactions and error handling.
- **`templates/index.html`**: HTML template that brings the chat interface to life.
- **`static/style.css`**: Custom CSS for styling, including dark mode support.
- **`static/script.js`**: JavaScript to manage chat input, communication with the AI backend, and real-time updates.

## 🚀 Get Started

1. Install the dependencies:
   ```bash
   pip install flask transformers
   ```
2. Launch the application:
   ```bash
   python app.py
   ```
3. Visit `http://localhost:5000` in your browser.
4. Start chatting with the AI!

## 🛠️ Requirements

- **Python** 3.7 or newer
- **Flask**:
   ```bash
   pip install flask
   ```
- **Transformers**:
   ```bash
   pip install transformers
   ```

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

## 🤝 Contribute to the Future of AI

We welcome your contributions! If you're interested in improving this interface or adding new features, feel free to submit a pull request. Together, we can make this project even better.