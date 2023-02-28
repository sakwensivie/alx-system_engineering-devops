#!/usr/bin/python3
''' Queries the Reddit API and returns the number of subscribers '''

import requests
import sys


def number_of_subscribers(subreddit):
    """ Queries to Reddit API """
    # User-Agent is a required header field that identifies the user agent
    u_agent = 'Mozilla/5.0'

    # headers is a dictionary of HTTP Headers to send with the Request
    headers = {
        'User-Agent': u_agent
    }

    # url is the url to send the request to
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return 0
    dic = res.json()
    if 'data' not in dic:
        return 0
    if 'subscribers' not in dic.get('data'):
        return 0
    return res.json()['data']['subscribers']
