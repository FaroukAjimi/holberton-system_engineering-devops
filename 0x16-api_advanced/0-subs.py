#!/usr/bin/python3
import json
import requests


def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': '1044@holbertonschool.com'
    }
    reddit = requests.get("https://www.reddit.com/r/{}.json"
                          .format(subreddit),
                          headers=headers)
    jsonred = reddit.json()
    try:
        s = (jsonred['data']['children'][1])['data']['subreddit_subscribers']
        return(s)
    except:
        return(0)
