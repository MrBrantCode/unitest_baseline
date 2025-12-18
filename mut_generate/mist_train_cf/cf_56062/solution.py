"""
QUESTION:
Write a function `total_substrings(s)` that calculates the total number of substrings without repeating characters in a string `s`. Given a list of strings, use this function to calculate the total number of substrings without repeating characters for each string and return the average count rounded to the nearest whole number. The function should not use any external libraries.
"""

def total_substrings(s):
    count = 0
    for i in range(len(s)):
        hash_map = {}
        for j in range(i, len(s)):
            if s[j] not in hash_map:
                count += 1
                hash_map[s[j]] = 1
            else:
                break
    return count