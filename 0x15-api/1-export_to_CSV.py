#!/usr/bin/python3
"""
Python script with REST API, for a given employee ID
returns Information about his/her TODO list
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    user_id = int(argv[1])
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    """ get user """
    for user in users:
        if user.get('id') == user_id:
            n_user = user

    """get todos """
    task_list = []
    for task in todos:
        if task.get('userId') == user_id:
            task_list.append(task)

    """find completed todos """
    completed_tasks = []
    for task in task_list:
        if task.get('completed') is True:
            completed_tasks.append(task)

    with open("{}.csv".format(user_id), 'w') as file:
        rules = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in task_list:
            rules.writerow([user_id, n_user.get('username'),
                           task.get('completed'), task.get('title')])
