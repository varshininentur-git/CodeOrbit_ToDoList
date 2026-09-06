"""A small Flask web application for managing a to-do list."""

from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)
# Flash messages need a secret key. Change this before deploying a real app.
app.config["SECRET_KEY"] = "todo-list-development-key"

# Store tasks in a Python list while the application is running.
tasks = []
TASKS_FILE = Path(__file__).with_name("tasks.txt")


def load_tasks():
    """Load saved tasks, if the text file already exists."""
    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            # Remove line endings and ignore blank lines from the saved file.
            tasks.extend(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        # No file yet simply means the list starts empty.
        pass
    except OSError:
        # The app can still run if the file cannot be read.
        app.logger.warning("Saved tasks could not be loaded.")


def save_tasks():
    """Write the current task list to the text file."""
    try:
        with TASKS_FILE.open("w", encoding="utf-8") as file:
            for task in tasks:
                file.write(f"{task}\n")
        return True
    except OSError:
        app.logger.warning("Tasks could not be saved.")
        return False


def add_task(task_name):
    """Validate and add a task. Returns a message category and text."""
    task_name = task_name.strip()
    if not task_name:
        return "error", "Error: Task cannot be empty."

    tasks.append(task_name)
    if not save_tasks():
        return "error", "Task was added, but it could not be saved to the file."
    return "success", "Task added successfully!"


def remove_task(task_index):
    """Remove one task by its zero-based list position."""
    if task_index < 0 or task_index >= len(tasks):
        return "error", "Error: Invalid task number."

    tasks.pop(task_index)
    if not save_tasks():
        return "error", "Task was removed, but the file could not be updated."
    return "success", "Task removed successfully!"


@app.route("/")
def index():
    """Show the form and the current numbered list of tasks."""
    return render_template("index.html", tasks=tasks)


@app.route("/add", methods=["POST"])
def add():
    """Receive a task from the form and return to the main page."""
    category, message = add_task(request.form.get("task", ""))
    flash(message, category)
    return redirect(url_for("index"))


@app.route("/remove/<int:task_index>", methods=["POST"])
def remove(task_index):
    """Remove the task belonging to the clicked Remove button."""
    category, message = remove_task(task_index)
    flash(message, category)
    return redirect(url_for("index"))


# Load saved tasks once when the web application starts.
load_tasks()


if __name__ == "__main__":
    app.run(debug=True)
