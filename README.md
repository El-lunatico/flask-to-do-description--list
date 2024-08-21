# Flask To-Do List Application

## Overview

This project is a simple to-do list web application built using Flask. It allows users to add tasks and their descriptions, which are then displayed on the page. The tasks and descriptions are stored in memory (in two lists) and displayed dynamically on the webpage using Jinja2 templating.

## Features

- **Add Task and Description**: Users can enter a task and its description through a form, which are then displayed on the webpage.
- **Dynamic Task List**: The tasks and their descriptions are displayed in a styled format on the webpage, with responsive design elements to handle different screen sizes.
- **Task Styling**: Tasks and descriptions are displayed in separate, well-styled containers for better readability.
- **User Input Handling**: Input fields for tasks and descriptions are designed with basic validation and user-friendly features like placeholder text.

## Installation and Setup

### Prerequisites

- Python 3.x
- Flask

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

Install the Flask framework using pip:

```bash
pip install flask
```

### Step 4: Run the Application

Run the Flask application by executing:

```bash
python app.py
```

The application will start running on `http://127.0.0.1:5000/`.

## File Structure

```
|-- app.py
|-- README.md
```

- **`app.py`**: The main Flask application file containing the route definitions and HTML template string.
- **`README.md`**: The file you are currently reading.

## Code Explanation

### `app.py`

The Flask application consists of two main routes:

1. **`/` (GET)**: Displays the form for entering tasks and the list of tasks that have been added.
2. **`/` (POST)**: Handles the form submission, appends the task and description to the respective lists, and re-renders the page.

The application uses in-memory lists (`listA` for tasks and `listB` for descriptions) to store the data.

### Styling

The application includes inline CSS within the HTML template to style the task list and form elements. The design is responsive and ensures the tasks and descriptions are displayed clearly and neatly.

## How to Use

1. **Open the Application**: Once the server is running, open your web browser and navigate to `http://127.0.0.1:5000/`.
2. **Add a Task**: Enter a task and its description in the form fields provided and click the "Add" button.
3. **View Tasks**: The tasks will be displayed below the form in a neatly styled format.

## Future Improvements

- **Persistent Storage**: Implement file-based or database storage to persist tasks across sessions.
- **Task Management**: Add features to edit and delete tasks.
- **Enhanced UI/UX**: Improve the design and user experience with additional styling and features.
- 
