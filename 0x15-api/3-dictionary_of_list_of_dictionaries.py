#!/usr/bin/python3
"""
python script that is using RESTapi for a given
employee id, returns information about is/her
TODO list
"""
import json
import requests
from sys import argv


if __name__ == '__main__':

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    d_user = {}
    d_username = {}

    for user in users:
        u_id = user.get('id')
        d_user[u_id] = []
        d_username[u_id] = user.get('username')

    for task in todos:
        task_dict = {}
        u_id = task.get('userId')
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = d_username.get(u_id)
        d_user[u_id].append(task_dict)

    with open("todo_all_employees.json", 'w') as file:
        json.dump(d_user, file)
