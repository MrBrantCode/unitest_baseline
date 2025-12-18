"""
QUESTION:
Implement a function named `process_table` that takes a table as input, where the table is a list of tuples containing information about a person in the format (name, alias, points, awake status). Filter the table to include only those persons with more than 100 points, sort the filtered table based on the person's name in ascending order, and return the sorted table.
"""

def process_table(table):
    # Filter the table to include only those persons with more than 100 points
    filtered_table = [person for person in table if person[2] > 100]

    # Sort the filtered table based on the person's name in ascending order
    sorted_table = sorted(filtered_table, key=lambda person: person[0])

    return sorted_table