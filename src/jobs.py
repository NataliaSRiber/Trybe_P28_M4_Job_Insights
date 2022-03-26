import csv

from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        jobs_reader = csv.DictReader(file)
        rows = []
        for row in jobs_reader:
            rows.append(row)
    return rows

# Fonte: https://docs.python.org/pt-br/3/library/
# csv.html
# Fonte: https://www.analyticsvidhya.com/blog/2021/
# 08/python-tutorial-working-with-csv-file-for-data-science/
