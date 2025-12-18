"""
QUESTION:
Write a function `select_and_sort_records` to select all records from a list of dictionaries where the 'name' is "John" and the 'age' is less than 30, then sort the selected records in ascending order by 'age'. The function takes a list of dictionaries as input and returns a list of dictionaries.
"""

def select_and_sort_records(records):
    return sorted([record for record in records if record['name'] == 'John' and record['age'] < 30], key=lambda x: x['age'])