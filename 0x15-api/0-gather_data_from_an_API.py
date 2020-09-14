#!/usr/bin/python3
"""  for a given employee ID, returns information """
import requests
from sys import argv


if __name__ == "__main__":
    get_ID = argv[1]
    the_URL = "https://jsonplaceholder.typicode.com/users/"
    employee = requests.get(the_URL + get_ID).json()
    get_name = employee.get('name')

    sec_URL = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(sec_URL).json()
    all_tasks = 0
    done_tasks = 0
    for i in todos:
        if str(i.get('userId')) == get_ID:
            all_tasks += 1
            if i.get('completed') is True:
                done_tasks += 1

    st_line = 'Employee {} is done with tasks({}/{}):'.format(get_name,
                                                              done_tasks,
                                                              all_tasks)
    print(st_line)
    for i in todos:
        if str(i.get('userId')) == get_ID:
            if i.get('completed') is True:
                get_TITLE = i.get('title')
                print("\t " + get_TITLE)
