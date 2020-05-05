#!/usr/bin/python3
import json
import requests
import sys
from collections import OrderedDict
if __name__ == '__main__':
    dta = OrderedDict()
    res1 = requests.get('https://jsonplaceholder.typicode.com/todos')
    res2 = requests.get('https://jsonplaceholder.typicode.com/users')
    s = res1.json()
    users = res2.json()
    for i in range(1, len(users) + 1):
        info = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(i))
        usern = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(i))
        username = usern.json().get('username')
        to = info.json()
        dta[str(i)] = []
        for d in to:
            ele = OrderedDict()
            ele['username'] = username
            ele['task'] = d.get('title')
            ele['completed'] = d.get('completed')
            dta[str(i)].append(ele)
    with open('todo_all_employees.json', 'w+', newline='') as f:
        json.dump(dta, f)
