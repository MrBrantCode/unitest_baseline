"""
QUESTION:
Write a function named `sort_table` that takes a list of dictionaries representing individuals with fields 'name', 'age', and 'profession'. The function should sort the table based on the 'age' field in descending order and then by the 'name' field in ascending order for individuals with the same age. The function should return the sorted table.

Note: The input table is a list of dictionaries, where each dictionary represents an individual with 'name', 'age', and 'profession' fields.
"""

def sort_table(table):
    return sorted(table, key=lambda x: (-x['age'], x['name']))