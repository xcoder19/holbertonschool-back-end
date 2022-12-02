#!/usr/bin/python3
"""api"""
import requests
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) == 2:
        id = int(sys.argv[1])

    url = "https://jsonplaceholder.typicode.com/"
    employee_name = ""

    try:
        response_users = requests.request("GET", "{}users/{}".format(url, id))
        response_tasks = requests.request("GET", "{}todos/".format(url))
        employee_name = response_users.json()["username"]

    except KeyError:
        pass

    total_number_of_tasks = len(response_tasks.json())

    with open('{}.json'.format(id), 'a') as f:
        f.write("{")
        f.write('"{}"'.format(id) + ":")
        f.write("[")
    try:
        count = 0
        for i in range(total_number_of_tasks):
            if response_tasks.json()[i]['userId'] == id:
                count += 1

        print(count)
        xcount = 0
        for i in range(total_number_of_tasks):
            dict = {}
            if response_tasks.json()[i]['userId'] == id:
                dict["task"] = response_tasks.json()[i]['title']
                dict["completed"] = response_tasks.json()[i]['completed']
                dict["username"] = employee_name

                with open('{}.json'.format(id), 'a') as f:
                    json.dump(dict, f)
                    if xcount + 1 < count:
                        f.write(",")
                        xcount += 1

        with open('{}.json'.format(id), 'a') as f:
            f.write("]")
            f.write("}")
    except NameError:
        pass
