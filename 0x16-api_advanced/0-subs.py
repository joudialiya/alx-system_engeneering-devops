#!/usr/bin/python3
"""Return the number of subs of a subreddit"""
import requests


def number_of_subscribers(subreddit):
    """Logic function"""
    result = requests.get("https://www.reddit.com/r/{}/about.json"
                          .format(subreddit),
                          headers={"User-Agent": "joudialiya-lagzal"},
                          allow_redirects=False)
    if result.status_code > 400:
        return 0
    return result.json().get("data").get("subscribers")
