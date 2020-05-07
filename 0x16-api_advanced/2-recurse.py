#!/usr/bin/python3
"""
top ten comments
"""

import json
import requests


def recurse(subreddit, hot_list=[]):
    """function that search for the best first
    ten hot comments"""
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': '1044@holbertonschool.com'
    }
    reddit = requests.get("https://www.reddit.com/r/{}/hot.json"
                          .format(subreddit),
                          headers=headers)
    jsonred = reddit.json()
    i = 0
    try:
        while (jsonred['data']['children'][i])['data']['title']:
            s = (jsonred['data']['children'][i])['data']['title']
            if s == "this sub doesn't exist":
                raise Exception
            hot_list.append(s)
            i = i + 1
    except:
        return(None)
    finally:
        return(hot_list)
