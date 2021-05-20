#!/usr/bin/python3
""" We'll just leave a happy little comment right here """
import requests


def number_of_subscribers(subreddit):
    """ give me your data """
    url = 'https://www.reddit.com/r/{}/about.json'
    head = {'User-Agent': 'This-doesnt-matter'}

    try:
        stuff = requests.get(url.format(subreddit), headers=head)
        jsonverofstuff = stuff.json().get('data').get('subscribers')
        return jsonverofstuff
    except Exception:
        return 0
