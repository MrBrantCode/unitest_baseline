"""
QUESTION:
Write a function `longest_frequency(strings)` that takes a list of strings as input and returns a tuple containing the longest string and its frequency. If there are multiple strings with the same maximum length, return the first one along with its frequency. If the list is empty, return (None, None). The function should return the frequency of the first occurrence in case of a tie.
"""

def longest_frequency(strings):
    if not strings: return (None, None)

    length_dict = {s: (len(s), strings.count(s)) for s in set(strings)}
    longest_str = max(length_dict, key=length_dict.get)

    return (longest_str, length_dict[longest_str][1])