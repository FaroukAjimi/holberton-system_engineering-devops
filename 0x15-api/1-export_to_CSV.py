#!/usr/bin/python3
import requests
import csv
import sys
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
                if key == 'completed' and value == True:
                    Done += 1
                    titles.append(i['title'])
with open('{}.csv'.format(int(arg)), 'w+') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for i in s:
        for key, value in i.items():
            if key == 'userId' and value == int(arg):
                writer.writerow([int(arg), usern, i['completed'], i['title']])
