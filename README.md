# Flask-to-do-description--list

## Overview

This Flask application provides a simple task management system using SQLite for data storage. This version includes updated features from the previous version, enhancing functionality with support for adding, editing, and deleting tasks through API endpoints.

## Features

- **View Tasks**: Displays a list of tasks with their titles and descriptions.
- **Add Task**: Allows users to add new tasks via a JSON-based POST request.
- **Edit Task**: Allows users to update existing tasks using their IDs.
- **Delete Task**: Allows users to delete tasks by specifying their IDs.
- **SQLite Database**: Tasks are stored in a SQLite database for persistent storage.
- **Improved Functionality**: This version includes additional features compared to the previous version, such as JSON-based interactions for task management.

## Installation and Setup

### Prerequisites

- Python 3.x
- Flask
- SQLite (included with Python's standard library)

### Step 1: Clone the Repository

Clone this repository to your local machine using:

```bash
git clone <repository-url>
```

### Step 2: Navigate to the Project Directory

```bash
cd <project-directory>
```

### Step 3: Install Required Python Packages

Install Flask using pip:

```bash
pip install flask
```

### Step 4: Run the Application

Run the Flask application by executing:

```bash
python app.py
```

The application will start running on `http://0.0.0.0:5000/`.

## File Structure

```
|-- app.py
|-- database.db
|-- templates
    |-- text_list.html
|-- README.md
```

- **`app.py`**: The main Flask application file containing route definitions and SQLite database operations.
- **`database.db`**: SQLite database file where tasks are stored (created automatically).
- **`templates/text_list.html`**: HTML template for rendering tasks (make sure this file exists).
- **`README.md`**: The file you are currently reading.

## Code Explanation

### `app.py`

- **`init_sqlite_db()`**: Initializes the SQLite database and creates the `task` table if it does not already exist.
- **`/` (GET)**: Fetches and displays all tasks from the database.
- **`/` (POST)**: Adds a new task to the database. Expects JSON data with `userInput` and `userInput2`.
- **`/get_task/<int:task_id>`**: Retrieves a specific task by its ID and returns it as JSON.
- **`/edit_task` (POST)**: Updates an existing task. Expects JSON data with `index`, `task`, and `description`.
- **`/delete_task/<int:task_id>` (POST)**: Deletes a task by its ID.

### HTML Template

The HTML template (`text_list.html`) should be created to render tasks. It should use Jinja2 templating to display tasks dynamically. Ensure this file is placed in the `templates` directory.

## API Endpoints

- **`GET /`**: Displays the list of tasks.
- **`POST /`**: Adds a new task (requires JSON payload with `userInput` and `userInput2`).
- **`GET /get_task/<task_id>`**: Retrieves a specific task (returns JSON with `task` and `description`).
- **`POST /edit_task`**: Edits an existing task (requires JSON payload with `index`, `task`, and `description`).
- **`POST /delete_task/<task_id>`**: Deletes a specific task by its ID.

## Updates from Previous Version

This update introduces the following new features:
- **JSON-Based Task Management**: Interact with tasks using JSON payloads for adding, editing, and deleting tasks.
- **Improved Database Operations**: Enhanced handling of database operations for task management.

## Future Improvements

- **User Authentication**: Add user authentication to manage tasks for individual users.
- **Task Categories**: Implement categories or tags for tasks.
- **Enhanced UI**: Improve the user interface with more styling and functionality.

## Troubleshooting

- **Database Issues**: Ensure `database.db` is created and accessible.
- **Missing Template**: Verify `text_list.html` is correctly placed in the `templates` directory.

---
