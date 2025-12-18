"""
QUESTION:
Write a function named `most_common_element` that takes a list of strings as input and returns the most common character among all the strings. The input list may contain up to 1 million strings, each with a maximum length of 100 characters. The strings are case-sensitive and can contain any printable ASCII characters. The solution should have a time complexity of O(n), where n is the total number of characters in all the strings combined.
"""

def most_common_element(strings):
    count_dict = {}

    for string in strings:
        for char in string:
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1

    max_count = 0
    most_common = None
    for char, count in count_dict.items():
        if count > max_count:
            max_count = count
            most_common = char

    return most_common