#!/usr/bin/env python

import psycopg2


def execute(req):

    # Connect to database
    db = psycopg2.connect("dbname=news")
    c = db.cursor()

    # Execute query
    c.execute(req)
    # Get data
    data = c.fetchall()
    db.close()
    # Return fetched data
    return data
