
---
# Flask-to-do-description--list with User Authentication

## Overview

This updated Flask application introduces user authentication and task management, enhancing the previous version with new features. It uses SQLite for persistent storage, securely hashes passwords, and manages user sessions. The application now includes a unique QR code generation feature that encodes the server's IP address for easy access.

## Features

- **User Authentication**: Secure registration and login with hashed passwords.
- **Task Management**: Add, edit, view, and delete tasks associated with individual users.
- **Session Management**: Users must be logged in to manage tasks, ensuring privacy and security.
- **QR Code Generation**: Automatically generates a QR code with the server’s IP address, providing a convenient way to access the application.
- **Immaculate Maturity**: Enhanced error handling and secure operations ensure a polished and reliable experience.

## Installation and Setup

### Prerequisites

- Python 3.x
- Flask
- SQLite (included with Python's standard library)
- `qrcode` library for QR code generation
- `werkzeug` library for password hashing

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone <repository-url>
```

### Step 2: Navigate to the Project Directory

```bash
cd <project-directory>
```

### Step 3: Install Required Python Packages

Install Flask, `qrcode`, and `werkzeug` using pip:

```bash
pip install flask qrcode[pil] werkzeug
```

### Step 4: Run the Application

Run the Flask application:

```bash
python app.py
```

The application will start running on `http://0.0.0.0:5000/`.

## File Structure

```
|-- app.py
|-- database.db
|-- templates
    |-- index.html
    |-- register.html
    |-- login.html
    |-- text_list.html
|-- README.md
```

- **`app.py`**: The main Flask application file with routes for user registration, login, task management, and QR code generation.
- **`database.db`**: SQLite database file where user and task data are stored (created automatically).
- **`templates/`**: Directory containing HTML templates for rendering views.
  - **`index.html`**: Homepage template.
  - **`register.html`**: Registration page template.
  - **`login.html`**: Login page template.
  - **`text_list.html`**: Template for displaying tasks.
- **`README.md`**: This file.

## Code Explanation

### `app.py`

- **`init_sqlite_db()`**: Initializes the SQLite database with `users` and `task` tables.
- **`/` (GET)**: Renders the homepage.
- **`/register`**: Handles user registration, creating a new user with a hashed password.
- **`/login`**: Handles user login, starting a session for authenticated users.
- **`/logout`**: Logs out the current user by clearing the session.
- **`/task`**: Displays tasks for the logged-in user.
- **`/add_task`**: Adds a new task for the logged-in user.
- **`/get_task/<task_id>`**: Retrieves a specific task for the logged-in user.
- **`/edit_task`**: Edits an existing task for the logged-in user.
- **`/delete_task/<task_id>`**: Deletes a specific task for the logged-in user.
- **QR Code Generation**: Encodes the server's IP address into a QR code for easy access.

## API Endpoints

- **`GET /`**: Displays the homepage.
- **`POST /register`**: Registers a new user (requires `username` and `password` in the form).
- **`POST /login`**: Logs in an existing user (requires `username` and `password` in the form).
- **`GET /logout`**: Logs out the current user.
- **`GET /task`**: Displays the tasks for the logged-in user.
- **`POST /add_task`**: Adds a new task (requires JSON payload with `userInput` and `userInput2`).
- **`GET /get_task/<task_id>`**: Retrieves a specific task (returns JSON with `task` and `description`).
- **`POST /edit_task`**: Edits an existing task (requires JSON payload with `index`, `task`, and `description`).
- **`POST /delete_task/<task_id>`**: Deletes a specific task (requires `task_id` in the URL).

## Updates from Previous Version

This updated version introduces:
- **User Authentication**: Secure user login and registration.
- **Session Management**: Maintains user sessions for task privacy.
- **QR Code Generation**: Encodes the server's IP address for quick access.

## Future Improvements

- **Enhanced UI**: Refine the user interface for a more polished look.
- **Advanced Features**: Add task categories, notifications, and integrations.

## Troubleshooting

- **Database Issues**: Ensure `database.db` is created and accessible.
- **Missing Templates**: Verify the presence of all required HTML files in the `templates` directory.

---
