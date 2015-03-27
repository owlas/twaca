#!/usr/bin/env python
'''
Created on 27 Mar 2015
Thanks to Will.

Simple module to generate HTML from the contents of the tweet database
'''

import MySQLdb
import datetime
import ConfigParser
import sys


def open_tag(tag, attributes = None):
    '''
    Return an HTML open tag. Include the attributes in no specified order.
    Attributes must be supplied as a dictionary, and so cannot have
    duplicate keys.
'''

    s = "<" + tag
    try:
        for key in attributes.keys():
            s += ' %s="%s"' % (key, attributes[key])
    except AttributeError:
        # attributes = None
        pass
    s += ">"

    return s


def close_tag(tag):
    '''
    Return an HTML close tag.
    '''
    return "</%s>" % tag


def full_tag(tag, content, attributes = None):
    '''
    Return an HMTL tag with specified content and attributes;
    attributes must be supplied as a dictionary.
    '''
    opener = open_tag(tag, attributes)

    # If there's no content, we need to close the tag
    if content is None:
        # Get rid of the closing '>'
        trunc = opener[:-1]
        return trunc + " />"
    else:
        return "%s%s</%s>" % (opener, content, tag)


def create_table(columns, data, attributes = None):
    '''
    Create a simple HTML table using the columns and data provided.
    The columns should be an iterable.  The data should be an iterable
    of iterables, each of the same length as the columns iterable.

    The attributes can only belong to the table itself.
    '''

    s = open_tag("table", attributes)
    s += open_tag("tr")
    for item in columns:
        s += full_tag("th", item)

    s += close_tag("tr")

    for row in data:
        row_string = open_tag("tr")
        for cell in row:
            row_string += full_tag("td", str(cell))
        row_string += close_tag("tr")
        s += row_string

    s += close_tag("table")

    return s


def query_db(hostname, username, password, database, query):
    '''
    Return results of the specified query, given the database connection details
    Returns a MySQLdb cursor.
    '''

    db = MySQLdb.connect(host=hostname, user=username, passwd=password, db=database)
    c = db.cursor()
    c.execute(query)

    result = c.fetchall()

    c.close()
    db.close()

    return result


def create_page(title, heading, col_names, result):
    '''
    Create a simple html page using the provided title, heading,
    column names and a set of results in some kind of 2D iterable
    structure.  The page will contain a heading, the time the
    page was written, and a table containing the provided info.

    Each item in the result must have the same length as the list
    of column names, or the table won't make sense.
    '''

    page = ""

    page += '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" ' + \
    '"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">'

    html_attrs = {"xmlns": "http://www.w3.org/1999/xhtml", "xml:lang": "en", "lang":"en"}
    page += open_tag("html", html_attrs)
    page += open_tag("head")
    page+= full_tag("meta", None, {"http-equiv": "Content-Type", "content": "text/html;charset=utf-8"})
    page += full_tag("title", title)
    page += close_tag("head")

    page += open_tag("body")
    page += full_tag("h2", heading)

    current_time = datetime.datetime.now()

    page += full_tag("p", "Page last updated: %s" % current_time)


    page += create_table(col_names, result, {"border": 1})

    page += close_tag("body")
    page += close_tag("html")

    return page


if __name__ == "__main__":

    if (len(sys.argv) != 2):
        print "Usage: python %s <path-to-config-file>" % sys.argv[0]
        sys.exit(1)

    cfg = ConfigParser.ConfigParser()
    cfg.read(sys.argv[1])


    # Configuration
    hostname = cfg.get("database", "hostname")
    database = cfg.get("database", "database")
    username = cfg.get("database", "username")
    password = cfg.get("database", "password")

    title = cfg.get("page", "title")
    heading = cfg.get("page", "heading")
    location = cfg.get("page", "location")

    table = cfg.get("query", "table")
    query = cfg.get("query", "query")
    columns = cfg.get("query", "columns").split(", ")

    result = query_db(hostname, username, password, database, query)

    page = create_page(title, heading, columns, result)

    f = open(location, "w")
    f.write(page)
    f.close()

