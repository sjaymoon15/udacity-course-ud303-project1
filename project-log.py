#!/usr/bin/env python3

import psycopg2

conn = psycopg2.connect("dbname=news user=postgres")

cur = conn.cursor()

cur.execute(
  """
  select count(articles.slug) num_articles, articles.title from articles
  join slug_from_path
  on articles.slug = slug_from_path.slug
  group by articles.slug, articles.title
  order by num_articles DESC
  limit 3;
"""
)

question1 = cur.fetchall()

print("### Solution for Question 1 (start)###")
for elem in question1:
    print(
        "{article_name} --- {num_views} views".format(
            article_name=elem[1], num_views=elem[0]
        )
    )
print("### Solution for Question 1 (end)###")
print("")

cur.execute(
  """
  select count(authors.id) num_authors, authors.name from articles
  join slug_from_path
  on articles.slug = slug_from_path.slug
  join authors
  on articles.author = authors.id
  group by authors.id, authors.name
  order by num_authors DESC
"""
)

question2 = cur.fetchall()

print("### Solution for Question 2 (start)###")
for elem in question2:
    print(
        "{author_name} --- {num_views} views".format(
            author_name=elem[1], num_views=elem[0]
        )
    )
print("### Solution for Question 2 (end)###")
print("")

cur.execute(
  """
  select
    ROUND(error_rate,2) error_rate, TO_CHAR(date::date,'Mon DD, YYYY') date
    from (
      select
      not_ok_status * 100.0 / (not_ok_status + ok_status) as error_rate, date,
      not_ok_status,
      ok_status
        from (
          select date_trunc('day', time) date, count(1),
          sum(case status when '200 OK' then 1 else 0 end) as ok_status,
          sum(case status when '200 OK' then 0 else 1 end) as not_ok_status
          from log
          group by date
        ) as num_status_table
      order by error_rate DESC
    ) as error_rate_table
  where error_rate > 1;
"""
)

question3 = cur.fetchall()

print("### Solution for Question 3 (start)###")
for elem in question3:
    print(
        "{date} --- {error_rate} % errors"
        .format(date=elem[1], error_rate=elem[0])
        )
print("### Solution for Question 3 (end)###")
print("")

cur.close()
conn.close()
