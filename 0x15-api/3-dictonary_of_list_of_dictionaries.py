#!/usr/bin/python3
import requests
import json
import sys
res1 = requests.get('https://jsonplaceholder.typicode.com/todos')
res2 = requests.get('https://jsonplaceholder.typicode.com/users')
s = res1.json()
users = []
usr = res2.json()
ict = []
for y in usr:
        users.append(y['username'])
for i in s:
        ict.append(i['userId'])
length = ict.count(1)
first = False
count=0
with open('to_do_all_employees.json', 'w+') as f:
        f.write('{')
        for u in users:
                count = 0
                first = False
                for i in s:
                        try:
                                for key, value in i.items():
                                        if key == 'userId' and value == users.index(u) + 1:
                                                if first == False:
                                                        f.write('"{}": ['.format(i['userId']))
                                                        first= True
                                                f.write(json.dumps({'task' : i['title'], 'completed': i['completed'], 'username': u}))
                                                count += 1
                                                if count != length:
                                                        f.write(", ")
                        except:
                                pass
                f.write(']}')
                if u != users[-1]:
                        f.write(', ')
