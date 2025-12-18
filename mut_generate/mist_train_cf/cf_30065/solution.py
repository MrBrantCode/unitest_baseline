"""
QUESTION:
Write a function `generate_payload` that takes in two parameters: `date_list`, a list of datetime.date objects, and `query`, a string representing the search query. The function should generate a payload for each date in the `date_list`, including the search query, sorting criteria, and a date range based on the date and the date 7 days prior to it, in the format `{'q': query + " sort:updated created:start_date..end_date"}`. Ensure the payloads are stored in a list and returned by the function.
"""

import datetime

def generate_payload(date_list, query):
    payloads = []
    for date in date_list:
        yesterday = date - datetime.timedelta(days=7)
        payload = {
            'q': query + " sort:updated" +
                 " created:%d-%02d-%02d..%d-%02d-%02d" % (yesterday.year, yesterday.month, yesterday.day, date.year, date.month, date.day)
        }
        payloads.append(payload)
    return payloads