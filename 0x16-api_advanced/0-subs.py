#!/usr/bin/env python3
# This program displays the number of subscribers of a subreddit


import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subreddits if any or return zero
    """
    base = "https://www.reddit.com/r/"
    url = f"{base}{subreddit}/about.json"

    headers = {"User-Agent": "MyAPI/0.0.1"}

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code in [302, 404]:
        return 0

    return res.json().get("data").get("subscribers")
