#!/usr/bin/python3
import csv
import requests
from sys import argv


def main():
    # Define the base API URI for the JSONPlaceholder API
    api_uri = "https://jsonplaceholder.typicode.com"

    # Get the user ID from the command-line argument
    user_id = argv[1]

    # Generate a filename for the CSV file using the user ID
    filename = f"{user_id}.csv"

    # Create the user URI by appending the user ID to the API URI
    user_uri = f"{api_uri}/users/{user_id}"

    # Create the todos URI
    todo_uri = f"{api_uri}/todos/"

    # Send a GET request to the user URI and parse the JSON response
    res = requests.get(user_uri).json()

    # Extract the username from the response
    user_name = res.get('username')

    # Send a GET request to the todos URI and parse the JSON response
    res = requests.get(todo_uri).json()

    # Filter todos to get only those belonging to the specified user ID
    user_todos = [todo for todo in res if todo['userId'] == int(user_id)]

    # Open a CSV file with write mode using the generated filename
    with open(filename, 'w') as csv_file:
        # Create a CSV writer
        csv_writer = csv.writer(csv_file)

        # Write a header row to the CSV file
        csv_writer.writerow(['User ID', 'Username', 'Status', 'Title'])

        # Iterate through user todos and write each todo as a row in the CSV
        for todo in user_todos:
            status = todo.get('completed')
            title = todo.get('title')
            csv_writer.writerow([user_id, user_name, status, title])


if __name__ == "__main__":
    try:
        # Check if the argument can be converted to an integer
        int(argv[1])
    except ValueError:
        # If the argument is not a valid integer, exit the script with an error code
        exit(1)

    # Call the main function
    main()
