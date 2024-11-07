import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, QAction, QLineEdit, QVBoxLayout, QWidget, QTextEdit, QDialog, QPushButton, QLabel, QToolButton
from PyQt5.QtCore import QUrl, QSize, Qt
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon, QFont, QPixmap

def generate_text_with_llama(prompt):
    command = ["ollama", "run", "llama3.2"]

    try:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate(input=prompt, timeout=30)

        if output:
            return output.strip()
        elif error:
            return f"Error occurred: {error.strip()}"
        else:
            return "No response received from the model."

    except subprocess.TimeoutExpired:
        process.kill()
        return "The request timed out. Please try again."

    except Exception as e:
        return f"An exception occurred: {str(e)}"

class ChatDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Network Buzz")
        self.setGeometry(400, 300, 500, 400)
        
        # Set up layout
        layout = QVBoxLayout()
        
        # Label for user input
        self.prompt_label = QLabel("Enter your prompt:")
        self.prompt_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #333;")
        layout.addWidget(self.prompt_label)
        
        # Text input for prompt with enhanced styling
        self.prompt_input = QLineEdit()
        self.prompt_input.setPlaceholderText("Type your question here...")
        self.prompt_input.setStyleSheet("""
            QLineEdit {
                color: #333;
                background-color: #ffffff;
                border: 2px solid #cccccc;
                border-radius: 10px;
                padding: 8px;
                font-size: 14px;
                transition: border-color 0.3s ease, box-shadow 0.3s ease;
            }
            QLineEdit:focus {
                border-color: #6c63ff;
                box-shadow: 0px 0px 10px rgba(108, 99, 255, 0.5);
            }
            QLineEdit:hover {
                border-color: #888;
            }
        """)
        layout.addWidget(self.prompt_input)
        
        # Text area to display responses
        self.response_display = QTextEdit()
        self.response_display.setReadOnly(True)
        self.response_display.setStyleSheet("""
            QTextEdit {
                background-color: #f9f9f9;
                color: #333;
                border: 1px solid #ddd;
                border-radius: 10px;
                padding: 10px;
                font-size: 14px;
            }
        """)
        layout.addWidget(self.response_display)
        
        # Send button with custom styling
        self.send_button = QPushButton("Send")
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #6c63ff;
                color: #fff;
                font-size: 14px;
                padding: 8px 16px;
                border-radius: 10px;
                border: none;
            }
            QPushButton:hover {
                background-color: #5a54d1;
            }
            QPushButton:pressed {
                background-color: #4b47b3;
            }
        """)
        self.send_button.clicked.connect(self.handle_send)
        layout.addWidget(self.send_button)
        
        self.setLayout(layout)
        
    def handle_send(self):
        prompt = self.prompt_input.text()
        if prompt:
            # User prompt displayed
            self.response_display.append(f"<b>User:</b> {prompt}\n")
            
            # Model's response generation
            response = generate_text_with_llama(prompt)
            
            # Display robot face with response
            self.add_robot_response(response)
            self.prompt_input.clear()

    def add_robot_response(self, response_text):
        """Display robot response with an icon."""
        # Load robot icon
        robot_icon = QPixmap("robot.png").scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        # Format text with image
        response_html = f"""
        <table>
            <tr>
                <td><img src="robot.png" width="30" height="30"></td>
                <td><b>Ollama:</b> {response_text}</td>
            </tr>
        </table>
        """
        self.response_display.append(response_html)

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Web Browser")
        self.setGeometry(300, 150, 900, 700)

        # Set up toolbar
        navbar = QToolBar("Navigation")
        navbar.setStyleSheet("background-color: #f0f0f0; padding: 3px;")
        navbar.setIconSize(QSize(30, 30))
        self.addToolBar(navbar)

        # Add buttons
        back_btn = QAction(QIcon("back.png"), "Back", self)
        back_btn.triggered.connect(self.browser_back)
        navbar.addAction(back_btn)

        forward_btn = QAction(QIcon("forward.png"), "Forward", self)
        forward_btn.triggered.connect(self.browser_forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction(QIcon("reload.png"), "Reload", self)
        reload_btn.triggered.connect(self.browser_reload)
        navbar.addAction(reload_btn)

        home_btn = QAction(QIcon("home.png"), "Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # "Network Buzz" button with custom styling
        chat_btn = QToolButton()
        chat_btn.setText("Network Buzz")
        chat_btn.setFixedSize(150, 50)  # Bigger size
        chat_btn.setStyleSheet("""
            QToolButton {
                background-color: #6c63ff;
                color: white;
                font-weight: bold;
                font-size: 16px;
                padding: 10px;
                border-radius: 5px;
            }
            QToolButton:hover {
                background-color: #5a54d1;
            }
            QToolButton:pressed {
                background-color: #4b47b3;
            }
        """)
        chat_btn.clicked.connect(self.open_chat)
        navbar.addWidget(chat_btn)

        # URL bar
        self.url_bar = QLineEdit()
        self.url_bar.setFont(QFont("Arial", 10))
        self.url_bar.setPlaceholderText("enter your url here")
        self.url_bar.setFixedWidth(400)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.url_bar.setStyleSheet("""
            QLineEdit {
                color: black;
                background-color: #ffffff;
                border-radius: 5px;
                padding: 4px;
                transition: box-shadow 0.3s ease;
            }
            QLineEdit:focus {
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
            }
        """)
        navbar.addWidget(self.url_bar)

        # Browser view
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))  # Set Glance homepage URL
        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        container.setLayout(layout)
        container.setStyleSheet("padding: 20px;")
        self.setCentralWidget(container)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #eaeaea;
            }
            QToolBar {
                spacing: 5px;
                height: 45px;
            }
            QToolBar QToolButton {
                color: black;
                background-color: #e0e0e0;
                border-radius: 5px;
                padding: 6px;
                margin: 3px;
            }
            QToolBar QToolButton:hover {
                background-color: #d0d0d0;
            }
        """)

    def open_chat(self):
        self.chat_dialog = ChatDialog()
        self.chat_dialog.exec_()

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))  # Navigate to Glance homepage

    def navigate_to_url(self):
        url = "http://" + self.url_bar.text().strip() + ".com"
        self.browser.setUrl(QUrl(url))

    def browser_back(self):
        self.browser.back()

    def browser_forward(self):
        self.browser.forward()

    def browser_reload(self):
        self.browser.reload()

app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec_())
