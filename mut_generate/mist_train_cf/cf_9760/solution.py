"""
QUESTION:
Write a function named `count_unique_substrings` that calculates the number of unique substrings possible with the given string, which may contain lowercase letters, uppercase letters, and digits, and its length will not exceed 1000 characters.
"""

def count_unique_substrings(string):
    substrings = set()
    n = len(string)
    
    for i in range(n):
        for j in range(i+1, n+1):
            substrings.add(string[i:j])
    
    return len(substrings)