# Level of difficulty
# Easy
#
# Estimated time
# 15 minutes
#
# Objectives
# improving the student's skills in interacting with the SQLite database;
# using known methods of the Cursor object.
# Scenario
# Our application requires you to add a little security and
#  display the data saved in the database. Your task is to implement
#  the following functionalities:
#
# Create a find_task method, which takes the task name as its argument.
# The method should return the record found or None otherwise.
# Block the ability to enter an empty task (the name cannot be an empty
# string).
# Block the ability to enter a task priority less than 1.
# Use the find_task method to block the ability to enter a task with the
# same name.
# Create a method called show_tasks, responsible for displaying all tasks
# saved in the database.
# Test data:
#
# Example input:
# Enter task name: My first task
# Enter priority: 1
#
# Example output:
# (1, 'My first task', 1)
#
# Example input:
# Enter task name: My second task
# Enter priority: 2
#
# Example output:
# (1, 'My first task', 1)
# (2, 'My second task', 2)
#
# Example input:
# Enter task name: My first task
# Enter priority: 1
#
# Example output:
# (1, 'My first task', 1)
# (2, 'My second task', 2)

import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect("todo.db")
        self.c = self.conn.cursor()
        self.create_tasks_table()

    def create_tasks_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def new_task(self):
        name = input("Enter task name: ")
        priority = int(input("Enter priority: "))

        if len(name) == 0 or priority < 1:
            return

        if self.find_task(name) is not None:
            return

        self.c.execute(
            '''INSERT INTO tasks (name, priority) VALUES (?,?)''',
            (name, priority))
        self.conn.commit()

    def find_task(self, name):
        self.c.execute('''SELECT * FROM tasks WHERE name = ?''', (name,))
        return self.c.fetchone()

    def show_tasks(self):
        for row in self.c.execute('''SELECT * FROM tasks'''):
            print(row)


app = Todo()
app.new_task()
app.show_tasks()
