#!/usr/bin/python3
"""
Export all users' todo data to a JSON file.
This script retrieves user information and their to-do list from a REST API
and exports it to a CSV file named after the user's ID.
"""
import json
import requests


def main():

    api_uri = "https://jsonplaceholder.typicode.com"  # Base URI for the API
    todo_res = requests.get(f"{api_uri}/todos").json()

    # Generate the filename for the JSON file
    filename = f"todo_all_employees.json"

    users_tasks = {}

    for user_id in range(1, 11):
        user_res = requests.get(f"{api_uri}/users/{user_id}").json()
        username = user_res.get('username')

        user_tasks = [todo for todo in todo_res
                      if todo['userId'] == user_id]

        tasks = []
        for task in user_tasks:
            t = {}
            t['username'] = username
            t['task'] = task.get('title')
            t['completed'] = task.get('completed')

            tasks.append(t)

        users_tasks[user_id] = tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(users_tasks, json_file)


if __name__ == "__main__":

    main()
