"""
QUESTION:
Implement a function named `find_unique_values` that takes a list of string and integer pairs as input, and returns a list of unique strings in descending order of their frequency of occurrence. If two strings have the same frequency, they should be ordered in ascending alphabetical order. The input list will not exceed 10^6 elements, the strings will consist of lowercase letters only, and the integers will be positive integers less than or equal to 10^6.
"""

def find_unique_values(dataset):
    frequency_dict = {}
    for pair in dataset:
        value = pair[0]
        if value in frequency_dict:
            frequency_dict[value] += 1
        else:
            frequency_dict[value] = 1

    sorted_values = sorted(frequency_dict.keys(), key=lambda x: (-frequency_dict[x], x))

    return sorted_values