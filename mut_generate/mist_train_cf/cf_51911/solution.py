"""
QUESTION:
Write a function `count_unique_substrings` that takes a string as input and returns the total number of unique substrings containing only unique characters. The string will consist of lowercase English letters and special symbols. Implement an algorithm with a time complexity better than O(n^2), where n is the length of the string.
"""

def count_unique_substrings(string):
    substr_count = 0
    visited = {}

    start = 0
    for end, char in enumerate(string):
        if char in visited:
            start = max(start, visited[char] + 1)

        substr_count += end - start + 1
        visited[char] = end
    
    return substr_count