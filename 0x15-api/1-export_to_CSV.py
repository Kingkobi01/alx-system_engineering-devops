#!/usr/bin/env python3
import csv
import requests
import sys

"""
Exports the data about the employee to a CSV file
"""


def main():
    """
    ...
    The Main Engine
    """

    def get_user_info(user_id):
        """
        ...
        Getting Employees Data
        """
        user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

        user_response = requests.get(user_url).json()

        user_name = user_response["name"]

        todos_url = "https://jsonplaceholder.typicode.com/todos"
        todos_response = requests.get(todos_url).json()

        user_todos = [todo for todo in todos_response if str(todo["userId"]) == user_id]

        return user_todos, user_name

    def export_to_CSV_file():
        """
        ...
        Exports it to a CSV File
        """
        user_todos = get_user_info(sys.argv[1])[0]
        username = get_user_info(sys.argv[1])[1]

        user_todos = [todo for todo in user_todos]

        with open(f"{sys.argv[1]}.csv", "w") as csv_file:
            field_names = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            csv_writer = csv.DictWriter(csv_file, field_names)

            for todo in user_todos:
                csv_writer.writerow(
                    {
                        "USER_ID": todo["userId"],
                        "USERNAME": username,
                        "TASK_COMPLETED_STATUS": todo["completed"],
                        "TASK_TITLE": todo["title"],
                    }
                )

    export_to_CSV_file()


if __name__ == "__main__":
    main()
