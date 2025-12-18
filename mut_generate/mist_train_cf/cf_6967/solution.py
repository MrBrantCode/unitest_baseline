"""
QUESTION:
Write a function named `lexicographical_order` that takes an array of strings as input and returns a list of unique strings in lexicographical order in descending order. The input array may contain duplicate strings and has a maximum length of 10^6.
"""

def lexicographical_order(arr):
    unique_strings = set()
    
    for string in arr:
        unique_strings.add(string)
    
    sorted_strings = sorted(unique_strings, reverse=True)
    
    return sorted_strings