"""
QUESTION:
Write a function `calculate_average_local_time` that takes a list of named tuples as input where each tuple has a field named 'local_time'. The function should return the average local time value by summing up all the local time values and dividing by the number of entries. If the list is empty, the function should return 0.0.
"""

def calculate_average_local_time(data):
    total_local_time = sum(float(entry.local_time) for entry in data)
    num_entries = len(data)
    return total_local_time / num_entries if num_entries > 0 else 0.0