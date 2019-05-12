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

# Days in which more than 1% of requests lead to errors


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
def printArticles():
    resultsAuthors = get_queryResults(requestArticles)
    print("Top 3 most popular articles of all time:\n")
    for title, views in resultsAuthors:
        print(title," - ",views," views")
    print("\n")

# Main function
if __name__ == '__main__':
    printArticles()