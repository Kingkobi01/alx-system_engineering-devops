#!/usr/bin/python3
import csv
import requests
from sys import argv
"""Exports the data about the employee to a CSV file
"""


def main():
    """...
    The Main Engine
    """

    api_uri = "https://jsonplaceholder.typicode.com"  # uri
    user_id = argv[1]  # id of user

    filename = f"{user_id}.csv"

    user_uri = f"{api_uri}/users/{user_id}"
    todo_uri = f"{api_uri}/todos/"
    res = requests.get(user_uri).json()

    user_name = res.get('username')  # username

    res = requests.get(todo_uri).json()

    user_todos = [todo for todo in res if todo['userId']
                  == int(user_id)]

    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        for todo in user_todos:
            status = todo.get('completed')
            title = todo.get('title')
            csv_writer.writerow([user_id, user_name, status, title])


if __name__ == "__main__":
    # Checks if the argument can be converted to an integer
    try:
        int(argv[1])
    except ValueError:
        exit(1)
    main()
