"""
QUESTION:
Develop a function named `is_shuffle_anagram` that takes three string parameters. The function should determine whether the third string is a shuffled version of the first two strings, i.e., an anagram of the combined first two strings. The function should return `True` if the third string is a correct shuffled anagram and `False` otherwise. The time complexity of the function should not exceed O(n log n), where n is the length of the third string.
"""

def is_shuffle_anagram(s1, s2, s3):
    # Check if the length of the third string is the sum of the first two
    if len(s3) != len(s1) + len(s2):
        return False
    # Combine the first two strings and sort them
    s1_s2_sorted = sorted(s1 + s2)
    # Also sort the third string
    s3_sorted = sorted(s3)
    # Compare the two sorted strings
    return s1_s2_sorted == s3_sorted