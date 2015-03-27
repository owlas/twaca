"""
Oliver W. Laslett
O.Laslett@soton.ac.uk
see LICENSE file


Given keywords it streams tweets
"""

from TwitterAPI import TwitterAPI

# First login
c_key = ''
c_sec = ''
a_key = ''
a_sec = ''

# Login and get the api object
api = TwitterAPI(c_key, c_sec, a_key, a_sec)

# Get football tweets
r = api.request('statuses/filter', {'track':'football,lithuania', 'filter_level':'none'})
for i in r.get_iterator():
    if 'text' in i:
        print i['user']['name']
        print i['user']['screen_name']
        print i['created_at']
        print i['favorite_count']
        print i['retweet_count']
        print i['user']['followers_count']
        print i['text']
