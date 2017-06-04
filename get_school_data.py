#!/usr/bin/env python

# Open data school directory
# https://data.delaware.gov/Education/School-Directory/wky5-77bt/data

SCHOOL_DIRECTORY_CSV_URL = (
    'https://data.delaware.gov/api/views/wky5-77bt/rows.csv')

import csv
from io import StringIO
import json

import requests

def main():
    with open('schools.lsjson', 'w') as fh:
        response = requests.get(SCHOOL_DIRECTORY_CSV_URL)
        data = response.content.decode('utf-8')
        reader = csv.DictReader(StringIO(data))
        rows = [json.dumps(dict(row)) + '\n' for row in reader]
        fh.writelines(rows)

if __name__ == '__main__':
    main()
