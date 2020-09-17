#!/usr/bin/python3
""" retrieves number of subscribers of subreddit """
import requests


def number_of_subscribers(subreddit):
    the_URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {"User-Agent": 'any agent'}

    data = requests.get(the_URL, headers=head, allow_redirects=False).json()
    if data is None:
        return 0
    data2 = data.get('data')
    if data2 is None:
        return 0
    return data2.get('subscribers')
