#!/usr/bin/python3

import psycopg2

# Queries
# Three most popular articles
requestArticles = (
    "select articles.title, count(*) as views "
    "from articles, log "
    "where articles.slug = substr(log.path, 10) "
    "group by articles.title "
    "order by views desc "
    "limit 3;"
)

# Most popular article authors
requestAuthors = (
    "select authors.name, count(*) as views "
    "from articles, authors, log "
    "where authors.id = articles.author "
    "and articles.slug = substr(log.path, 10) "
    "group by authors.name "
    "order by views desc;"
)

# Days in which more than 1% of requests lead to errors
requestErrorDays = (
    "select day, errorpercent "
    "from errorpercent "
    "where errorpercent > 1;"
)

# Database query function
# Opens connection, executes query, closes connection.


def get_queryResults(query_request):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query_request)
    results = c.fetchall()
    db.close()
    return results

# Print report


def printReport():
    resultsArticles = get_queryResults(requestArticles)
    resultsAuthors = get_queryResults(requestAuthors)
    resultsErrorDays = get_queryResults(requestErrorDays)

    print("Top 3 most popular articles of all time:\n")
    for title, views in resultsArticles:
        print("{:<35}{:^3}{:>15} views".format(title, "-", views))
    print("\n")

    print("Most popular authors:\n")
    for authors, views in resultsAuthors:
        print("{:<35}{:^3}{:>15} views".format(authors, "-", views))
    print("\n")

    print("Days with more than 1 percent error rate in requests:\n")
    for day, errorpercent in resultsErrorDays:
        print("{:<35}{:^3}{:>15} percent".format(
            str(day), "-", round(errorpercent, 5)))
    print("\n")

# Main function


if __name__ == '__main__':
    printReport()
