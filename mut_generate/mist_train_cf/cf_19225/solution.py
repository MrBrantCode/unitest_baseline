"""
QUESTION:
Write a function named `count_and_sort` that takes a list of strings as input. The function should convert all strings to lowercase, remove duplicates, count the occurrences of each unique string, and return the sorted list of unique strings and their counts in descending order of counts.
"""

def count_and_sort(strings):
    # Convert all values to lowercase
    lower_strings = [x.lower() for x in strings]

    # Count the number of occurrences of each element
    counts = {x: lower_strings.count(x) for x in set(lower_strings)}

    # Sort the list by the number of occurrences in descending order
    sorted_list = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_list