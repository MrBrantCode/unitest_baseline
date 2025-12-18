"""
QUESTION:
Create a function named `sort_dictionary_by_length` that takes a dictionary containing names and ages of people as input, and returns a dictionary sorted by the sum of the length of the names and ages in descending order. If two or more people have the same sum of lengths, they should be sorted alphabetically by name in ascending order. The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def sort_dictionary_by_length(dictionary):
    data = []
    for name, age in dictionary.items():
        sum_of_lengths = len(name) + len(str(age))
        data.append((name, age, sum_of_lengths))
    data.sort(key=lambda x: (-x[2], x[0]))
    sorted_dict = {}
    for name, age, _ in data:
        sorted_dict[name] = age
    return sorted_dict