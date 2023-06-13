#!/usr/bin/python3
""" Function that queries the Reddit API
    and prints the first top ten hot post of a subreddit"""
import requests
import sys
after = None
count_dic = []


def count_words(subreddit, word_list):
    global after
    global count_dic
    headers = {'User-Agent': 'xica369'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)
