"""
QUESTION:
Given a string `s` and an integer `k`, write a function named `count_substrings` that returns the number of substrings in `s` that contain exactly `k` different characters.
"""

def count_substrings(string, k):
    counter = 0

    # Iterate through all possible substrings
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            unique_chars = set(substring)

            # If the number of unique characters is equal to k, increment the counter
            if len(unique_chars) == k:
                counter += 1

    return counter