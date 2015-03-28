"""
Oliver W. Laslett
O.Laslett@soton.ac.uk
see LICENSE file


Given keywords it streams tweets
"""

from TwitterAPI import TwitterAPI
import MySQLdb as mdb
import argparse

# Get keyword from the command line
parser = argparse.ArgumentParser(description=
                                 "Collect real-time tweets related to your keyword and archive them in an SQL database")
parser.add_argument('keywords', type=str, nargs='+', help="Define the tracking keywords for collecting tweets")
args = parser.parse_args()
keywords = ''.join([a + ',' for a in args.keywords])
keywords.rstrip(',')

# First login
c_key = ''
c_sec = ''
a_key = ''
a_sec = ''

# Login and get the api object
api = TwitterAPI(c_key, c_sec, a_key, a_sec)

# Open SQL database and get the cursor
con = mdb.connect('localhost', 'pythonapp', 'pypass', 'tweet');

# Function to strip non-ascii chars
def strip_non_ascii(string):
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

# Get football tweets
with con:
    r = api.request('statuses/filter', {'track':keywords, 'filter_level':'none'})
    cur = con.cursor()
    for i in r.get_iterator():
        if 'text' in i:
            cur.execute("INSERT INTO tweet VALUES(%s,%s,%s,%s,%s,%s,%s,%s);",
                        (strip_non_ascii(i['id_str']),
                         strip_non_ascii(i['user']['name']),
                         strip_non_ascii(i['user']['screen_name']),
                         strip_non_ascii(i['text']),
                         strip_non_ascii(i['created_at']),
                         strip_non_ascii(' '.join([h['text']+' ' for h in i['entities']['hashtags']])),
                         strip_non_ascii(' '.join([u['expanded_url']+' ' for u in i['entities']['urls']])),
                         str(i['user']['followers_count'])))
            con.commit()
