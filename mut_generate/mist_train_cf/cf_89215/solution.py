"""
QUESTION:
Create a function named `sort_dictionary_by_length` that takes a dictionary where keys are names and values are ages as input, and returns a new dictionary sorted by the sum of the lengths of the names and ages in descending order. If two or more people have the same sum of lengths, they should be sorted alphabetically by name in ascending order. The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def sort_dictionary_by_length(dictionary):
    data = [(name, age, len(name) + len(str(age))) for name, age in dictionary.items()]
    data.sort(key=lambda x: (-x[2], x[0]))
    return {name: age for name, age, _ in data}