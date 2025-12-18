"""
QUESTION:
Write a function `search_substrings(string, substrings)` that searches for multiple substrings in a given string and returns a list of index positions of each substring found in the string. The function should handle cases where the substrings appear multiple times in the string, overlapping substrings, and have a time complexity of O(n), where n is the length of the string, without using any built-in functions or libraries for string search or substring matching.
"""

def search_substrings(string, substrings):
    positions = []
    string_length = len(string)
    substring_lengths = [len(substring) for substring in substrings]
    
    for i in range(string_length):
        for j in range(len(substrings)):
            if string[i:i+substring_lengths[j]] == substrings[j]:
                positions.append(i)
    
    return positions