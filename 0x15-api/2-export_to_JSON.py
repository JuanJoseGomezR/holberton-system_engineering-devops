#!/usr/bin/python3
""" CDV Format """

import json
import requests
from sys import argv


if __name__ == "__main__":
    get_ID = argv[1]
    the_URL = "https://jsonplaceholder.typicode.com/users/"
    employee = requests.get(the_URL + get_ID).json()
    get_name = employee.get('username')

    sec_URL = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(sec_URL).json()

    new_list = []
    for i in todos:
        new_dict = {}
        if str(i.get('userId')) == get_ID:
            get_status = i.get('completed')
            get_title = i.get('title')
            new_dict["task"] = get_title
            new_dict["completed"] = get_status
            new_dict["username"] = get_name
            new_list.append(new_dict)

    emp_dict = {get_ID: new_list}
    jason = get_ID + ".json"
    with open(jason, 'w') as file:
        file.write(json.dumps(emp_dict))
