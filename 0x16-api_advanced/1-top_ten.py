#!/usr/bin/python3
"""
This program queries the Reddit API and
returns the tiles for the top ten posts
for a given subreddit.

If an invalid subreddit is given,
the function should return 0.
"""


import requests


def top_ten(subreddit):
    """
    Return the number of subreddits if any or return zero
    """
    base = "https://www.reddit.com/r/"
    url = f"{base}{subreddit}/top.json"

    headers = {"User-Agent": "MyAPI/0.0.1"}

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code in [302, 404]:
        print(None)

    top_ten_posts = [
        post.get("data")["title"]
        for post in res.json().get("data").get("children")[:10]
    ]

    for title in top_ten_posts:
        print(title)
