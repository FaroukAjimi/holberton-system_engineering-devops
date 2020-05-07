#!/usr/bin/python3
import json
import requests


def top_ten(subreddit):
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': '1044@holbertonschool.com'
    }
    reddit = requests.get("https://www.reddit.com/r/{}/hot.json"
                          .format(subreddit),
                          headers=headers)
    jsonred = reddit.json()
    try:
        for i in range(10):
            s = (jsonred['data']['children'][i])['data']['title']
            if s == "this sub doesn't exist":
                raise Exception
            print(s)
    except:
        print(None)
