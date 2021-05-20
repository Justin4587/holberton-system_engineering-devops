#!/usr/bin/python3
""" We'll just leave a happy little comment right here """
import requests


def top_ten(subreddit):
    """ give me your data """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'
    head = {'User-Agent': 'This-doesnt-matter'}

    try:
        stuff = requests.get(url.format(subreddit), headers=head,
                             allow_redirects=False).json()
        stuffplus = stuff.get('data').get('children')
        for titles in stuffplus:
            print(titles.get('data').get('title'))
    except Exception:
        pass
