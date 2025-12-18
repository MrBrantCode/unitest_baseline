"""
QUESTION:
Write a function named `find_most_frequent_name` that takes an array of names as input and returns the name that appears most frequently. The array can contain up to 10^6 names. The function must have a time complexity of O(n), where n is the number of names in the array.
"""

def find_most_frequent_name(names):
    frequency = {}
    max_frequency = 0
    most_frequent_name = ""

    for name in names:
        if name in frequency:
            frequency[name] += 1
        else:
            frequency[name] = 1

        if frequency[name] > max_frequency:
            max_frequency = frequency[name]
            most_frequent_name = name

    return most_frequent_name