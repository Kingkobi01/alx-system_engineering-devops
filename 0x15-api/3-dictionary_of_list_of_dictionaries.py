#!/usr/bin/python3
"""
Export user's todo data to a CSV file.
This script retrieves user information and their to-do list from a REST API
and exports it to a CSV file named after the user's ID.
"""
import json
import requests


def main():

    api_uri = "https://jsonplaceholder.typicode.com"  # Base URI for the API

    # Generate the filename for the CSV file (e.g., '2.csv')
    filename = f"todo_all_employees.json"

    json_array = []

    for user_id in range(1, 11):
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
            task['username'] = user_name
            task['task'] = todo.get('title')
            task['completed'] = todo.get('completed')
            user_todos_for_json.append(task)

        user_data = {user_id: user_todos_for_json}
        json_array.append(user_data)

    # Write user's to-do data to a CSV file
    with open(filename, 'w', encoding='utf-8', newline='') as json_file:
        json.dump(json_array, json_file)


if __name__ == "__main__":

    main()
