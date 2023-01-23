# Task Tracker App
This is a simple task tracking app built using Flask and Bootstrap. The app allows the user to:

- Start and stop tasks by task ID
- Add and edit tasks with a task ID and description
- Display a list of all tasks and their current status (running or stopped)
- Display a graph of all tasks and their cumulative time and cycles

## Installation
To install the app and it's dependencies run: 

```bash
python setup.py install
``` 

## Getting Started
To run the app, you will need to have Python3 and Flask installed. Once you have those, you can clone this repository and run the following command to start the app:

```bash
flask run
```

Then, open your browser and navigate to http://localhost:5000 to access the app.

## Usage
The app has four main pages:

**Home:** Allows you to start and stop tasks by selecting the task ID from a dropdown list and clicking the corresponding button.

**Display Tasks:** Shows a table of all tasks and their current status, description, cycles, and cumulative time.

**Graph Tasks:** Shows a graph of all tasks and their cumulative time and cycles.

**Add/Edit Tasks:** Allows you to add or edit tasks by entering a task ID and description and clicking the corresponding button.

## Built With
- Python
- Flask
- Bootstrap

## Issues and Improvements
Feel free to create issues to raise awareness of problems or feature implementation requests.

By all means please contribute fixes and features through pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.