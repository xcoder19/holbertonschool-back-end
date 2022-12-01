#!/usr/bin/python3
"""api"""
import requests
import sys


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
with open('{}.csv'.format(id), 'w') as f:
    try:
        for i in range(total_number_of_tasks):
            if response_tasks.json()[i]['userId'] == id:

                f.write(
                    '"{}",'.format(id) +
                    '"{}",'.format(employee_name) +
                    '"{}",'.format(
                        response_tasks.json()[i]['completed']) +
                    '"{}"'.format(
                        response_tasks.json()[i]['title'])


                )
                f.write('\n')
    except NameError:
        pass
