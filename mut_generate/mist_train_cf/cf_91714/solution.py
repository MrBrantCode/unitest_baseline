"""
QUESTION:
Develop a function `search_substrings` that takes two parameters: a string and a list of substrings. The function should return a list of index positions of each substring found in the string, handling multiple occurrences and overlapping substrings, with a time complexity of O(n), where n is the length of the string, and without using any built-in functions or libraries for string search or substring matching.
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