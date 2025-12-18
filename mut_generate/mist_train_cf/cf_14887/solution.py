"""
QUESTION:
Write a function `count_substrings` that takes a string and an integer `k` as input and returns the number of substrings with exactly `k` different characters.
"""

def count_substrings(string, k):
    counter = 0

    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            unique_chars = set(substring)

            if len(unique_chars) == k:
                counter += 1

    return counter