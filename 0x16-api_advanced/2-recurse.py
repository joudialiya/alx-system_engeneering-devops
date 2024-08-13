#!/usr/bin/python3
"""Returns hot posts"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Logic function"""
    result = requests.get("https://www.reddit.com/r/{}/hot.json"
                          .format(subreddit),
                          params={"after": after},
                          headers={"User-Agent": "joudialiya-lagzal-2"},
                          allow_redirects=False)
    if result.status_code < 400:
        hot_list = [hot_list,
                    [hot.get("data").get("title")
                     for hot in result.json().get("data").get("children")]]
        return recurse(subreddit,
                       hot_list,
                       result.json().get("data").get("after"))
    if len(hot_list) == 0:
        return None
    return hot_list
