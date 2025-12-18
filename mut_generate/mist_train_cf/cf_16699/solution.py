"""
QUESTION:
Create a function `sort_strings(strings, alphabetical_order)` to sort a list of strings based on a given alphabetical order defined by a dictionary where each letter is associated with a unique integer value. The sorting should be performed in a way that the strings are arranged in ascending order based on the sum of the integer values of the characters in each string. If two strings have the same sum, they should be sorted based on their length in descending order. If two strings have the same sum and length, they should be sorted in lexicographical order. If a string contains characters that are not present in the alphabetical order dictionary, consider the character's value as 0 for sorting purposes.
"""

def sort_strings(strings, alphabetical_order):
    def get_key(s):
        sum_val = sum(alphabetical_order.get(c, 0) for c in s)
        return (sum_val, -len(s), s)

    return sorted(strings, key=get_key)