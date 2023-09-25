#!/usr/bin/env python3
import pprint
import requests
import sys


def main():
    def get_user_info(user_id):

        user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

        user_response = requests.get(user_url).json()

        user_name = user_response["name"]

        todos_url = "https://jsonplaceholder.typicode.com/todos"
        todos_response = requests.get(todos_url).json()

        # pprint.pprint(todos_response)

        user_todos = [todo for todo in todos_response if str(todo["userId"]) == user_id]

        completed_tasks = [todo for todo in user_todos if todo["completed"]]
        total_todos = len(user_todos)

        print(
            f"Employee {user_name} is done with tasks({len(completed_tasks)}/{total_todos}):"
        )

        for todo in completed_tasks:
            print(f"     {todo['title']}")

    get_user_info(sys.argv[1])


if __name__ == "__main__":
    main()
