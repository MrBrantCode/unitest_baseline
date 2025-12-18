"""
QUESTION:
Implement a function called `find_unique_john_records` that takes a list of dictionaries as input where each dictionary represents a record with a 'name' and a 'surname'. The function should return a list of unique records with the name "John" sorted alphabetically by their surname. Use lambda expressions and higher order functions for your solution and avoid using traditional control flow methods.
"""

def find_unique_john_records(records):
    return sorted(
        list({x['surname']: x for x in filter(lambda x: x['name'] == 'John', records)}.values()), 
        key=lambda x: x['surname']
    )