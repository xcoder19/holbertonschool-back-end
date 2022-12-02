#!/usr/bin/python3
"""api"""
import json
import requests
import sys


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    response_users = requests.request("GET", "{}users".format(url))
    response_tasks = requests.request("GET", "{}todos".format(url))
    users_json = response_users.json()
    tasks_json = response_tasks.json()
    array = []
    for user in users_json:

        userId = user['id']
        username = user['username']

        for task in tasks_json:
            if task['userId'] == userId:
                tasks_dict = {}
                tasks_dict["username"] = username
                tasks_dict["task"] = task["title"]
                tasks_dict["completed"] = task["completed"]
                array.append(tasks_dict)

dict = {}
try:
    for user in users_json:
        userId = user['id']
        username = user['username']
        arr = []
        for i in array:
            if i['username'] == username:
                arr.append(i)
        dict[userId] = arr

    with open("todo_all_employees.json", "w") as file:
        json.dump(dict, file)
except NameError:
    pass
