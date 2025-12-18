"""
QUESTION:
Write a function `find_substring_frequency(text, substring)` that determines the frequency of a specific dynamic substring within the provided string. The substring can vary in length from 2 to 6 characters and will always be provided in alphabetical order. The function should consider overlapping occurrences and return the frequency count.
"""

def find_substring_frequency(text, substring):
    count = 0
    N = len(text)
    M = len(substring)
    sorted_substring = ''.join(sorted(substring))
    for i in range(N - M + 1):
        if ''.join(sorted(text[i:i+M])) == sorted_substring:
            count += 1
    return count