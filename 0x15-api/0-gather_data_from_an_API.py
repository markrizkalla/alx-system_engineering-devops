#!/usr/bin/python3
"""Python script using this REST API, for a given
employee ID,returns information about his TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    id = int(sys.argv[1])
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    user_name = users[id - 1].get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    completed_todos = []
    total_todos = 0
    for todo in todos:
        if todo.get('userId') == id:

            total_todos += 1

            if todo.get('completed'):
                completed_todos.append(todo.get('title'))

    print(f"Employee {user_name} is done with"
          f"tasks({len(completed_todos)}/{total_todos}):")

    for todo in completed_todos:
        print('     ' + todo)
