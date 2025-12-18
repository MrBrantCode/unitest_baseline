"""
QUESTION:
Write a function named `filter_and_sort` that takes a list of strings as input. The function should filter out strings that are empty or contain only whitespace characters, remove duplicate strings in a case-insensitive manner, and return the resulting list in reverse alphabetical order.
"""

def filter_and_sort(strings):
    filtered_list = [s.strip() for s in strings if s.strip() != ""]
    deduplicated_list = list(set([s.lower() for s in filtered_list]))
    sorted_list = sorted(deduplicated_list, reverse=True)
    return sorted_list