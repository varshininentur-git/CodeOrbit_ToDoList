# 📝 To-Do List

A simple and beginner-friendly **To-Do List web application** built using Python, Flask, HTML, and CSS. The application allows users to add, view, and remove tasks while saving tasks to a text file.

## ✨ Features

* ➕ Add new tasks
* 👀 View all tasks
* 🗑️ Remove tasks
* 🔢 Display tasks in a numbered list
* 💾 Save tasks to a text file
* 🔄 Load saved tasks when the application starts
* ⚠️ Handle empty task input
* 🎨 Clean and responsive user interface
* 🌐 Web-based application
* 🐍 Python and Flask backend
* 📝 HTML and CSS frontend

## 🛠️ Technologies Used

| Technology | Purpose           |
| ---------- | ----------------- |
| Python     | Application logic |
| Flask      | Web framework     |
| HTML5      | Webpage structure |
| CSS3       | Styling           |
| Text File  | Store tasks       |

## 📁 Project Structure

```text
CodeOrbit-Task3/
│
├── app.py
├── tasks.txt
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

## ⚙️ How It Works

1. Open the To-Do List application in a web browser.
2. Enter a task in the input field.
3. Click the **Add Task** button.
4. The task is added to the task list.
5. Tasks are displayed as a numbered list.
6. Click **Remove** to delete a task.
7. Tasks are saved in `tasks.txt`.
8. Previously saved tasks are loaded when the application starts.

## ➕ Adding a Task

Enter a task in the input box:

```text
Complete Python assignment
```

Click **Add Task**.

The task will appear in the list:

```text
Your Tasks

1. Complete Python assignment
```

The application also saves the task to `tasks.txt`.

## 🗑️ Removing a Task

Each task has a **Remove** button.

For example:

```text
1. Complete Python assignment    [Remove]
2. Study for exam               [Remove]
3. Finish project               [Remove]
```

Clicking **Remove** deletes the selected task and updates the saved task list.

## 🚨 Error Handling

The application handles empty task input.

If the user tries to add an empty task, the application displays:

```text
Error: Task cannot be empty.
```

The application also handles missing task files without crashing.

## 💾 Task Storage

Tasks are stored in:

```text
tasks.txt
```

The application loads saved tasks when it starts and updates the file whenever a task is added or removed.

## 💻 Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Go into the project folder:

```bash
cd CodeOrbit-Task3
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask application:

```bash
python3 app.py
```

You should see:

```text
* Running on http://127.0.0.1:5000
```

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

## 🧪 Example

```text
TO-DO LIST

[ Enter a new task... ] [ Add Task ]

Your Tasks

1. Complete Python assignment       [Remove]
2. Study for exam                  [Remove]
3. Finish project                  [Remove]
```

## 🎯 Learning Objectives

This project demonstrates:

* Python programming
* Flask web development
* HTML forms
* CSS styling
* Python lists
* Functions
* File handling
* Reading and writing text files
* User input validation
* Flask routing
* Connecting a Python backend with an HTML frontend

## 🚀 Future Improvements

Possible future improvements include:

* Mark tasks as completed
* Edit existing tasks
* Add task deadlines
* Add task priorities
* Add categories
* Add dark mode
* Add a database
* Add user accounts
* Add JavaScript for a more interactive interface
