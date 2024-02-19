#!/usr/bin/python3
"""Python script to export data in the CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":

    id = int(sys.argv[1])
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(url + '/users').json()
    user_name = users[id - 1].get('username')

    tasks = requests.get(url + '/todos').json()

    with open(str(id) + ".csv", 'w', newline="") as f:
        spamwriter = csv.writer(f, quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in tasks:
            if task.get('userId') == id:
                spamwriter.writerow([str(id), user_name,
                                    str(task.get('completed')),
                                    task.get('title')])
