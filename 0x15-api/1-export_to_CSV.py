#!/usr/bin/python3
"""
Export user's todo data to a CSV file.
This script retrieves user information and their to-do list from a REST API
and exports it to a CSV file named after the user's ID.
"""
import csv
import requests
from sys import argv


def main():

    api_uri = "https://jsonplaceholder.typicode.com"  # Base URI for the API
    user_id = argv[1]  # User ID provided as a command-line argument

    # Generate the filename for the CSV file (e.g., '2.csv')
    filename = f"{user_id}.csv"

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

    # Write user's to-do data to a CSV file
    with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
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
