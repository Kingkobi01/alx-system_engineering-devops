#!/usr/bin/python3
"""
Export user's todo data to a JSON file.
This script retrieves user information and their to-do list from a REST API
and exports it to a JSON file named after the user's ID.
"""
import json
import requests
from sys import argv


def main():

    api_uri = "https://jsonplaceholder.typicode.com"  # Base URI for the API
    user_id = argv[1]  # User ID provided as a command-line argument

    # Generate the filename for the JSON file (e.g., '2.json')
    filename = f"{user_id}.json"

    # Retrieve user information from the API
    user_uri = f"{api_uri}/users/{user_id}"
    todo_uri = f"{api_uri}/todos/"
    user_info = requests.get(user_uri).json()

    # Extract user's username
    user_name = user_info.get('username')

    # Retrieve all to-do items from the API
    todos = requests.get(todo_uri).json()

    # Filter to-do items for the specified user
    user_todos = [todo for todo in todos if todo['userId'] == int(user_id)]

    user_todos_for_json = []

    for todo in user_todos:
        task = {}
        task['task'] = todo.get('title')
        task['completed'] = todo.get('completed')
        task['username'] = user_name
        user_todos_for_json.append(task)

    # Write user's to-do data to a JSON file
    with open(filename, 'w', encoding='utf-8', newline='') as json_file:
        json_data = {user_id: user_todos_for_json}
        json.dump(json_data, json_file)


if __name__ == "__main__":
    # Checks if the argument can be converted to an integer
    try:
        int(argv[1])
    except ValueError:
        exit(1)
    main()
