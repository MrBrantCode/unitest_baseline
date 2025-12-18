"""
QUESTION:
Write a function `longest_substring` that takes a string as input and returns the longest substring without any repeating characters. The function should store the last seen indices of characters and update the starting point of the substring when a repeating character is found, keeping track of the longest seen substring without repeating characters.
"""

def longest_substring(s):
    seen = {}
    longest = [0,1]
    start = 0
    for i, character in enumerate(s):
        if character in seen and start <= seen[character]:
            start = seen[character]+1
        else:
            if i+1-start > longest[1]-longest[0]:
                longest = [start, i+1]
        seen[character] = i
    return s[longest[0]:longest[1]]