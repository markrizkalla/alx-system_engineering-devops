#!/usr/bin/python3
"""Python script using REST API"""
import requests
import sys

if __name__ == "__main__":
    id = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(url + '/users').json()
    user_name = users[id - 1].get('name')

    todos = requests.get(url + '/todos').json()
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
        print('\t ' + todo)
