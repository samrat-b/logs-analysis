#!/usr/bin/env python

from logsdb import execute


def most_pop_art():
    req = """
    select title, count(log.id) as hits
    from articles, log
    where slug = substring(path, 10)
    group by title
    order by hits desc
    limit 3;
    """
    data = execute(req)
    print(" Most popular three articles of all time: \n")
    for i, d in enumerate(data):
        article = str(d[0])
        hits = str(d[1])
        print('\t "' + article + '"' + ' -> ' + hits + ' views \n')


def pop_art_auth():
    req = """
    select name, sum(hits) as hits from
    (select articles.author as author, title, count(log.id) as hits
    from articles, log
    where slug = substring(path, 10)
    group by articles.author, title) as popart, authors
    where popart.author = authors.id
    group by name
    order by hits desc;
    """
    data = execute(req)
    print(" Most popular article authors of all time: \n")
    for i, d in enumerate(data):
        name = str(d[0])
        hits = str(d[1])
        print('\t "' + name + '"' + ' -> ' + hits + ' views \n')


def err_logs():
    req = """
    select to_char(date(time), 'Mon dd, yyyy') as date,
    round(100.00*errval/totalval,2) as calcval from
    (select count(time) as totalval, date(time) as totaldate
    from log group by totaldate ) as totallog,
    (select count(time) as errval, date(time) as errdate
    from log where status like '%404%'
    group by errdate) as errlog, log
    where totaldate = errdate and date(time) = errdate
    and errval > (totalval*1)/100
    group by date, calcval;
    """
    data = execute(req)
    print(" Days on which more than 1% of requests lead to errors: \n")
    for i, d in enumerate(data):
        date = str(d[0])
        percent = str(d[1])
        print('\t "' + date + '"' + ' -> ' + percent + ' percent \n')


if __name__ == '__main__':
    # Output data fetched from database
    most_pop_art()
    pop_art_auth()
    err_logs()
