#!/usr/bin/env python

import psycopg2
DBNAME = "news"


def run_query(query):
    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def get_most_viewed_articles():
    query = """
        SELECT
            articles.title,
            COUNT(*) AS views
        FROM
            articles
        INNER JOIN
            log
        ON
            log.path = '/article/' || articles.slug
        WHERE
            log.status like '200%'
        GROUP BY
            articles.title
        ORDER BY
            views DESC
        LIMIT
            3;
    """

    results = run_query(query)

    print('\nWhat are the most popular three articles of all time?\n')
    count = 1
    for i in results:
        number = str(count) + '.'
        title = i[0]
        views = ' - ' + str(i[1]) + " views"
        print(number + title + views)
        count += 1


def get_most_viewed_authors():

    query = """
        SELECT
            authors.name,
            COUNT(*) AS views
        FROM
            authors
        INNER JOIN
            articles
        ON
            authors.id = articles.author
        INNER JOIN
            log
        ON
            log.path = '/article/' || articles.slug
        WHERE
            log.status like '200%'
        GROUP BY
            authors.name
        ORDER BY
            views DESC
        LIMIT
            3;
    """

    results = run_query(query)

    print('\nWho are the most popular authors?\n')
    count = 1
    for i in results:
        print(str(count) + '.' + i[0] + ' - ' + str(i[1]) + " views")
        count += 1


def get_days_with_most_errors():

    query = """
                SELECT day, perc FROM (
                    SELECT a.day, ROUND(
                        CAST((100*b.requests) as numeric) /
                        CAST(a.requests as numeric), 2) as perc FROM (
                        SELECT date(time) as day,
                        count(*) as requests FROM log group by day) as a,
                        (SELECT date(time) as day, count(*) as requests
                    FROM
                        log
                    WHERE
                        status not like '%200%' group by day) as b
                    WHERE
                        a.day = b.day) as perc
                WHERE
                    perc > 1.0;
    """

    results = run_query(query)

    print('\nWhich days had more then 1% errors?\n')
    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1], 3)) + "% errors"
        print(date + " - " + errors)


print('Getting Results...')
get_most_viewed_articles()
get_most_viewed_authors()
get_days_with_most_errors()
