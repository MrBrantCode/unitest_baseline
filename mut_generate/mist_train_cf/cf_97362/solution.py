"""
QUESTION:
Write a function named `count_substrings` that takes two parameters: a string and an integer `k`, and returns the number of substrings with exactly `k` different alphabetical characters, ignoring any non-alphabetical characters in the string.
"""

def count_substrings(s, k):
    cleaned_string = ''.join(char for char in s if char.isalpha())
    count = 0
    for i in range(len(cleaned_string)):
        for j in range(i+1, len(cleaned_string)+1):
            if len(set(cleaned_string[i:j])) == k:
                count += 1
    return count