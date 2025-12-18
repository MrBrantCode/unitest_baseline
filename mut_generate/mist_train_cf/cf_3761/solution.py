"""
QUESTION:
Write a function `select_john` that takes a list of dictionaries as input. The function should return a list of dictionaries where the 'name' is 'John' and the 'age' is less than 30. The 'age' attribute must exist and be an integer in the selected records. The returned list should be sorted in ascending order by the 'age' attribute.
"""

def select_john(records):
    return sorted([record for record in records if record.get('name') == 'John' and isinstance(record.get('age'), int) and record.get('age') < 30], key=lambda record: record.get('age'))