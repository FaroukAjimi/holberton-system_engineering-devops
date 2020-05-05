#!/usr/bin/python3
import json
import requests
import sys
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        dta = OrderedDict()
        res1 = requests.get('https://jsonplaceholder.typicode.com/todos')
        res2 = requests.get('https://jsonplaceholder.typicode.com/users')
        s = res1.json()
        users = res2.json()
        for i in range(1, len(users) + 1):
            info = request.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'
                .format(i))
            usern = request.get(
                'https://jsonplaceholder.typicode.com/users/{}'.format(i))
            username = usern.json().get('username')
            to = info.json()
            dta[str(i)] = []
            for d in to:
                ele = OrderedDict()
                ele['username'] = username
                ele['task'] = d.get('title')
                ele['completed'] = d.get('completed')
                data[str(i)].append(ele)
        with open('todoall_employees.json', 'w+', newline='') as f:
            json.dump(dta, f)
