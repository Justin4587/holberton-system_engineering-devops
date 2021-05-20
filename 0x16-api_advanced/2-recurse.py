#!/usr/bin/python3
""" We'll just leave a happy little comment right here """
import requests


def recurse(subreddit, hot_list=[], extra=""):
    """ give me your data """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=1'
    head = {'User-Agent': 'This-doesnt-matter'}

    stuff = requests.get(url.format(subreddit, extra), headers=head,
                         allow_redirects=False).json()
    """try:
            if stuff.status_code != 200 or stuff == "None":
                print(None)
                return
        except Exception:
        pass"""
    stuffplus = stuff.get('data').get('children')
    for titles in stuffplus:
        hot_list.append(titles.get('data').get('title'))
    extra = stuff.get('data').get('extra')
    if extra is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, extra)
