#!/usr/bin/python3
"""Given an Employee ID, returns information
about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == '__main__':
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = f'{api_url}/users/{emp_id}'
    todo_uri = f'{user_uri}/todos'

    # User Response
    res = requests.get(user_uri).json()

    # Name of the employee
    name = res.get('name')

    # User TODO Response
    res = requests.get(todo_uri).json()

    # Total number of tasks, the sum of completed and non-completed tasks
    total = len(res)

    # Number of non-completed tasks
    non_completed = sum([elem['completed'] is False for elem in res])

    # Number of completed tasks
    completed = total - non_completed

    # Formatting the expected output
    str = f"Employee {name} is done with tasks({completed}/{total}):"
    print(str)

    # Printing completed tasks
    for elem in res:
        if elem.get('completed') is True:
            print('\t ', elem.get('title'))
