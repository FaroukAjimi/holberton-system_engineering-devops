#!/usr/bin/python3
import requests
import json
import sys
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        arg = sys.argv[1]
        res1 = requests.get('https://jsonplaceholder.typicode.com/todos')
        res2 = requests.get('https://jsonplaceholder.typicode.com/users')
        s = res1.json()
        usr = res2.json()
        for y in usr:
            if y['id'] == int(arg):
                user = y['name']
                usern = y['username']
        Max = 0
        Done = 0
        titles = []
        for i in s:
            for key, value in i.items():
                if key == 'userId' and value == int(arg):
                    Max += 1
                    for key, value in i.items():
                        if key == 'completed' and value is True:
                            Done += 1
                            titles.append(i['title'])
        c = 0
        with open('{}.json'.format(int(arg)), 'w+') as f:
            f.write('{')
            f.write('"{}": ['.format(int(arg)))
            for i in s:
                for key, value in i.items():
                    if key == 'userId' and value == int(arg):
                        c += 1
                        f.write(json.dumps({'task': i['title'],
                                            'completed': i['completed'],
                                            'username': usern}))
                        if c != Max:
                            f.write(", ")
            f.write(']}')
