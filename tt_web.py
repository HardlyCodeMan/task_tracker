from flask import Flask, render_template, request
import json
import time

app = Flask(__name__)

class Task:
    def __init__(self, task_id, description):
        self.id = task_id
        self.description = description
        self.started = False
        self.start_time = None
        self.cycles = 0
        self.cumulative_time = 0

    def start(self):
        if not self.started:
            self.started = True
            self.start_time = int(time.time())
            return f"Task {self.id} has been started."
        else:
            return f"Task {self.id} is already running."

    def stop(self):
        if self.started:
            current_time = int(time.time())
            self.started = False
            self.cumulative_time += current_time - self.start_time
            self.cycles += 1
            return f"Task {self.id} has been stopped. Time spent: {current_time - self.start_time} seconds."
        else:
            return f"Task {self.id} is not currently running."

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            task_data = json.load(file)
        tasks = []
        for task in task_data:
            tasks.append(Task(task["id"], task["description"]))
            tasks[-1].started = task["started"]
            tasks[-1].start_time = task["start_time"]
            tasks[-1].cycles = task["cycles"]
            tasks[-1].cumulative_time = task["cumulative_time"]
        return tasks
    except:
        return []

def save_tasks(tasks):
    task_data = []
    for task in tasks:
        task_data.append({"id": task.id, "description": task.description, "started": task.started, "start_time": task.start_time, "cycles": task.cycles, "cumulative_time": task.cumulative_time})
    with open("tasks.json", "w") as file:
        json.dump(task_data, file)

@app.route("/")
def index():
    tasks = load_tasks()
    running_tasks = [task for task in tasks if task.started]
    return render_template("index.html", running_tasks=running_tasks, all_tasks=tasks)

@app.route("/start", methods=["POST"])
def start():
    task_id = int(request.form["task_id"])
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            result = task.start()
            save_tasks(tasks)
            return render_template("result.html", result=result)
    return render_template("result.html", result="Invalid task id.")

@app.route("/stop", methods=["POST"])
def stop():
    task_id = int(request.form["task_id"])
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            result = task.stop()
            save_tasks(tasks)
            return render_template("result.html", result=result)
    return render_template("result.html", result="Invalid task id.")

@app.route("/add_edit", methods=["POST"])
def add_edit():
    task_id = int(request.form["task_id"])
    task_desc = request.form["task_desc"]
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            task.description = task_desc
            save_tasks(tasks)
            return render_template("result.html", result=f"Task {task_id} has been edited.")
    tasks.append(Task(task_id, task_desc))
    save_tasks(tasks)
    return render_template("result.html", result=f"Task {task_id} has been added.")

@app.route("/display")
def display():
    tasks = load_tasks()
    return render_template("display.html", task_list=tasks)

@app.route("/graph")
def graph():
    tasks = load_tasks()
    return render_template("graph.html", task_list=tasks)

if __name__ == "__main__":
    app.run(debug=True)