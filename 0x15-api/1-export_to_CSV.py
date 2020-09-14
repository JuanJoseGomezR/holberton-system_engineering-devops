#!/usr/bin/python3
""" export data in the CSV format """

import csv
import requests
from sys import argv

if __name__ == "__main__":
    get_ID = argv[1]
    the_URL = "https://jsonplaceholder.typicode.com/users/"
    employee = requests.get(the_URL + get_ID).json()
    get_name = employee.get('username')

    sec_URL = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(sec_URL).json()

    cSv = get_ID + ".csv"
    with open(cSv, 'w', newline='') as file:
        write = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC,)
        for i in todos:
            if str(i.get('userId')) == get_ID:
                status_task = str(i.get('completed'))
                get_title = i.get('title')
                write.writerow([get_ID, get_name, status_task, get_title])
