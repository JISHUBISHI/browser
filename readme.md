# Network Buzz - PyQt Web Browser and Chat Bot

## Description

Network Buzz is a desktop application built with PyQt5 that combines a fully functional web browser with an integrated chat bot. The chat bot uses a local Llama model (accessed via the `ollama` CLI) to generate responses to user questions. The application features a modern and responsive UI with a custom-styled chat dialog and navigation toolbar.

## Features

- **Web Browser:**  
  - Navigate web pages using a QWebEngineView.
  - Toolbar buttons for Back, Forward, Reload, and Home navigation.
  - URL input bar for direct URL entry.

- **Integrated Chat Bot:**  
  - Launch a chat dialog to ask questions.
  - Uses a local Llama model (`llama3.2`) for text generation.
  - Displays both user queries and bot responses with styled HTML formatting and icons.
  
- **Custom UI:**  
  - Modern, clean UI with custom styles for dialogs, buttons, and input fields.
  - Supports both text-based chat and traditional browsing within the same application.

## Requirements

- Python 3.7+
- [PyQt5](https://pypi.org/project/PyQt5/)
- [PyQtWebEngine](https://pypi.org/project/PyQtWebEngine/)
- A local installation of the `ollama` CLI tool and the `llama3.2` model.
- Optional: Custom icons (`back.png`, `forward.png`, `reload.png`, `home.png`, and `robot.png`) placed in the same directory as the application for enhanced UI visuals.

## Installation

1. **Clone the Repository**
   git clone https:https://github.com/JISHUBISHI/browser
   cd browser
Create a Virtual Environment (Recommended)


## Install Dependencies
## bash

pip install -r requirements.txt
## Set Up Llama Model

Ensure that you have the ollama CLI installed and that the llama3.2 model is available. For installation and setup instructions, refer to the Ollama documentation.



## Place the following icon image files in the project directory:

back.png
forward.png
reload.png
home.png
robot.png
These icons enhance the user interface for navigation and chat.

## How It Works
Browser Component
The Browser class extends QMainWindow and sets up:
A navigation toolbar with buttons (Back, Forward, Reload, Home) and a URL input field.
A QWebEngineView to load and display web pages.
## Chat Component
The ChatDialog class extends QDialog and provides:
A text input field for user questions.
A read-only text display area for conversation history.
A "Send" button that triggers the text generation process.
The generate_text_with_llama function calls the ollama CLI with the llama3.2 model and a user prompt (appending "in 30 words" for concise answers). It captures and returns the generated text, handling any errors or timeouts.
## Application Flow
Launch the application to open the main browser window.
Use the toolbar to navigate to different web pages.
Click the "💬 Network Buzz" button to open the chat dialog.
In the chat dialog, type your question and press "Send" to receive a response from the Llama model.
Both user queries and model responses are displayed in the chat dialog with custom formatting.
Running the Application
After completing the installation steps, run the application with:

## bash
python your_script_name.py
Replace your_script_name.py with the filename containing the provided code. The main browser window will launch, allowing you to browse the web and interact with the integrated chat bot.


## Author
Agnik Bishi and Parthib Karak - Developers of Network Buzz
