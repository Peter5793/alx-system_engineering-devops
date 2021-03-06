#!/usr/bin/python3
"""
Using the REST API, for a given employee ID return
information about his/her TODO list progress
"""
import json
import requests
from sys import argv


if __name__ == '__main__':

    user_id = int(argv[1])
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    for user in users:
        if user.get('id') == user_id:
            n_user = user

    task_list = []
    for task in todos:
        if task.get('userId') == user_id:
            task_list.append(task)

    n_dict = {}
    list_dict = []

    for n_task in task_list:
        task_dict = {}
        task_dict['task'] = n_task.get('title')
        task_dict['completed'] = n_task.get('completed')
        task_dict['username'] = n_user.get('username')
        list_dict.append(task_dict)

    n_dict[user_id] = list_dict

    """ create json file """
    with open("{}.json".format(user_id), "w") as file:
        json.dump(n_dict, file)
