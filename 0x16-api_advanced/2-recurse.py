#!/usr/bin/python3
"""
recursion comments
"""

import json
import requests


def recurse(subreddit, hot_list=[], next=""):
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
    try:
        hot_list.extend(jsonred['data']['children'])
        next = jsonred['data']['after']
        if jsonred['data']['after'] is None:
            return
    except:
        return(None)
    getfoward(subreddit, hot_list, next)
    return(hot_list)


def getfoward(subreddit, hot_list=[], next=""):
    """getting all next pages"""
    if next is None:
        return
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'From': '1044@holbertonschool.com'
    }
    reddit = requests.get("https://www.reddit.com/r/{}/hot.json"
                          .format(subreddit),
                          headers=headers,
                          params={'after': next, 'limit': 100})
    jsonred = reddit.json()
    hot_list.extend(jsonred['data']['children'])
    return getfoward(subreddit, hot_list, jsonred['data']['after'])
