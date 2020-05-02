# Log Analysis

To create a reporting tool that prints out reports (in plain text) based on the data in the database.

## Questions the reporting tool should answer

```
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Example:

July 29, 2016 — 2.5% errors
```

## Datebase tables

### log table

![log_table](/log_table.png)

### articles table

![articles_table](/articles_table.png)

### authors table

![authors_table](/authors_table.png)

## Relationship Diagram

![relationship_diagram](/diagram.png)

## Download the data

[Click here to download news database!](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

After download the database file newsdata.zip, set up the database

```
$ psql -d news -f newsdata.sql
```

## Create view

```
create or replace view slug_from_path as
  select split_part(path, 'article/', 2) as slug, * from log;
```

## Getting started

```
$ python3 project-log.py
```

## Source code file

```
project-log.py
```

## Example Output file

```
example_output.txt
```
