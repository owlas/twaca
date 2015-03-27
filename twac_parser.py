from TwitterAPI import TwitterAPI
import MySQLdb as mdb
import operator

popularity = {} 

class Hashtag:
    def __init__(self,string):
        self.string = string

    def return_hashtags(self):
        splitted_line = self.string.split()
        return splitted_line

con = mdb.connect('localhost', 'twacpy', 'twacpy15', 'tweet');
cursor = con.cursor()
cursor.execute('SELECT hashtags FROM tweet')
rows = cursor.fetchall()
for i in rows:
    for n in i:
        if not n == '':
            hashtag = Hashtag(n)
            hashtags = hashtag.return_hashtags()
            for ii in hashtags:
                if not ii in popularity:
                    popularity[ii] = 1
                else:
                    popularity[ii] += 1
sorted_popularity = sorted(popularity.items(),key=operator.itemgetter(1))
log_data = sorted_popularity[-11:-1]
logfile = '/root/twacademia/logfile.txt'
f = open(logfile,'w')
for i in log_data:
    f.write(str(i[0]) + '   ' + str(i[1]) + '\n')
f.close()
