"""
QUESTION:
Write a function named `parse_university_data` that takes a JSON string representing a list of university data as input. The function should parse the data, calculate the ratio of graduates to students for each university, round the ratio to two decimal places, rank the universities based on the ratio in descending order, and return a list of dictionaries containing the country, faculty, number of students, number of graduates, the ratio of graduates to students, and the rank.
"""

import json
from operator import itemgetter

def parse_university_data(universities_json):
    universities = json.loads(universities_json)

    # calculate ratio and add it to each university dict
    for university in universities:
        ratio = round(university['graduates'] / university['students'], 2)
        university['ratio'] = ratio

    # rank the universities based on the ratio
    universities.sort(key=itemgetter('ratio'), reverse=True)

    # add rank to each university dict
    for i, university in enumerate(universities, start=1):
        university['rank'] = i

    return universities