#!/usr/bin/python3
"""Returns hot posts"""
import requests


def top_ten(subreddit):
    """Logic function"""
    result = requests.get("https://www.reddit.com/r/{}/hot.json"
                          .format(subreddit),
                          headers={"User-Agent": "joudialiya-lagzal"},
                          allow_redirects=False)
    if result.status_code > 400:
        print("None")
    return [print(hot.get("data").get("title"))
            for hot in result.json().get("data").get("children")]
