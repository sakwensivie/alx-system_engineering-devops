#!/usr/bin/python3
""" Function taht queries the Reddit API
and prints the titles of the first 10
 hot posts listed for a given subreddit. """
import requests
import sys


def top_ten(subreddit):
    """Queries to Reddit API"""
    # the user agent is a required header field that identifies the user agent
    # what is the user agent?
    # the user agent is a string that identifies
    # the browser, operating system, and application
    # version of the user's computer
    u_agent = 'Mozilla/5.0'

    # headers is a dictionary of HTTP Headers to send with the Request
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'limit': 10
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)
    if res.status_code != 200:
        print(None)
        return
    dic = res.json()
    hot_posts = dic['data']['children']
    if len(hot_posts) is 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
