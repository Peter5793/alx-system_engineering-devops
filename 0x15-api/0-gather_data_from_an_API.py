#!/usr/bin/python3
"""
Python script with REST API, for a given employee ID
returns Information about his/her TODO list
"""
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

    """ print based on format stated"""
    print("Employee {} is done with tasks({}/{}):".format(n_user.get('name'),
                                                          len(completed_tasks),
                                                          len(task_list)))

    for print_task in completed_tasks:
        print("\t {}".format(print_task.get('title')))
