"""
QUESTION:
Write a function `sort_records` to sort records from a database table based on four columns: `age` in descending order, `name` in ascending order, `salary` in descending order, and `department` in ascending order. The function should return the sorted records.
"""

def sort_records(records):
    """
    Sorts records from a database table based on four columns: 
    `age` in descending order, `name` in ascending order, 
    `salary` in descending order, and `department` in ascending order.

    Args:
    records (list): A list of dictionaries where each dictionary represents a record.

    Returns:
    list: The sorted records.
    """
    return sorted(records, key=lambda x: (-x['age'], x['name'], -x['salary'], x['department']))