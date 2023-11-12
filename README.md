# Azubi-GPT Chatbot Documentation

## Introduction

Azubi-GPT is a simple chatbot designed to answer user queries based on a set of predefined questions and responses. This documentation provides an overview of how to use the chatbot and describes the functions used in the application.

## Table of Contents 
1. [Getting Started](#getting-started) 
	- [Installation](#installation)
	- [Running the Chatbot](#running-the-chatbot) 
2. [Chatbot Features](#chatbot-features) 
	- [User Interface](#user-interface) 
	- [Sending Messages](#sending-messages) 
	- [Admin Panel](#admin-panel) 
3. [ChatGui Class](#chatgui-class) 
	- [__init__ Method](#__init__-method) 
	- [send_message Method](#send_message-method) 
	- [show_admin_login Method](#show_admin_login-method) 
4. [SimpleChatbot Class](#simplechatbot-class) 
	- [__init__ Method](#__init__-method) 
	- [get_response Method](#get_response-method) 
	- [add_response Method](#add_response-method) 
5. [AdminPanel Class](#adminpanel-class) 
	- [__init__ Method](#__init__-method) 
	- [add_edit_response Method](#add_edit_response-method) 
6. [AdminLogin Class](#adminlogin-class)
	- [__init__ Method](#__init__-method) 
	- [login Method](#login-method)


## Getting Started
This documentation provides a quick guide on installing and using the Azubi-GPT chatbot. Users can interact with the chatbot through the provided user interface, and admins can access an admin panel for managing responses. The functions described give an overview of the functionality and usage of the chatbot's main features.

### Installation

To use the Azubi-GPT chatbot, follow these steps:

1. Clone the Azubi-GPT repository from GitHub:

   ```bash
   git clone https://github.com/your_username/Azubi-GPT.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Azubi-GPT
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Chatbot

Run the chatbot application using the following command:

```bash
python main.py
```

## Chatbot Features

### User Interface

The chatbot features a simple user interface with a message history area, an input field for user messages, and buttons for sending messages and accessing the admin panel.

### Sending Messages

Users can interact with the chatbot by typing their messages in the input field and clicking the "Send" button. The chatbot will respond with predefined answers based on the user's input.

### Admin Panel

Clicking the "Admin" button opens an admin login window. Admins can log in and access an admin panel for managing chatbot responses.

## `ChatGui` Class
- - -
### Methods

### `__init__`

- **Description:** Initializes the ChatGUI class.
- **Parameters:**
  - `master`: The Tkinter master window.
- **Usage:**
  ```python
  gui = ChatGUI(master)
  ```

### `send_message`

- **Description:** Sends a user message to the chatbot and displays the response in the message history.
- **Parameters:** None
- **Usage:**
  ```python
  gui.send_message()
  ```

### `show_admin_login`

- **Description:** Displays the admin login window.
- **Parameters:** None
- **Usage:**
  ```python
  gui.show_admin_login()
  ```


---

## `SimpleChatbot` Class

### Description

The `SimpleChatbot` class is responsible for handling user queries and providing responses based on predefined question-answer pairs.

### Methods

#### `__init__(self)`

- **Description:** Initializes the SimpleChatbot class with a set of predefined question-answer pairs.
- **Parameters:** None
- **Usage:**
  ```python
  chatbot = SimpleChatbot()
  ```

#### `get_response(self, user_input)`

- **Description:** Retrieves a response from the chatbot based on the user's input.
- **Parameters:**
  - `user_input` (str): The user's input query.
- **Returns:** The chatbot's response.
- **Usage:**
  ```python
  response = chatbot.get_response("What is Azubi Africa?")
  ```

#### `add_response(self, question, response)`

- **Description:** Adds a new question-answer pair to the chatbot's knowledge base.
- **Parameters:**
  - `question` (str): The new question to be added.
  - `response` (str): The corresponding response to the question.
- **Usage:**
  ```python
  chatbot.add_response("new question", "new response")
  ```

---

## `AdminPanel` Class

### Description

The `AdminPanel` class provides an admin interface for adding or editing question-answer pairs in the chatbot's knowledge base.

### Methods

#### `__init__(self, master, chatbot)`

- **Description:** Initializes the AdminPanel class.
- **Parameters:**
  - `master`: The Tkinter master window.
  - `chatbot`: An instance of the SimpleChatbot class.
- **Usage:**
  ```python
  admin_panel = AdminPanel(master, chatbot)
  ```

#### `add_edit_response(self)`

- **Description:** Adds or edits a question-answer pair in the chatbot's knowledge base.
- **Parameters:** None
- **Usage:**
  ```python
  admin_panel.add_edit_response()
  ```

---

## `AdminLogin` Class

### Description

The `AdminLogin` class provides a login interface for accessing the admin panel.

### Methods

#### `__init__(self, master, chatbot)`

- **Description:** Initializes the AdminLogin class.
- **Parameters:**
  - `master`: The Tkinter master window.
  - `chatbot`: An instance of the SimpleChatbot class.
- **Usage:**
  ```python
  admin_login = AdminLogin(master, chatbot)
  ```

#### `login(self)`

- **Description:** Handles the login process and opens the admin panel if the credentials are correct.
- **Parameters:** None
- **Usage:**
  ```python
  admin_login.login()
  ```
