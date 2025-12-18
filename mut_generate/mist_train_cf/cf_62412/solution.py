"""
QUESTION:
Write a function `check_anagram_samples` that determines if a given string can be partitioned into two or more substrings which are anagrams of each other. The function should take a string as input and return a boolean value indicating whether the string can be partitioned into anagrams. The function should not check for partitions of size greater than half the length of the original string.
"""

from collections import Counter

def check_anagram_samples(text: str) -> bool:
    """ Given a string, decide if it can be partitioned into two or more substrings which are anagrams of each other """
    length = len(text)
    for size in range(1, length // 2 + 1):  # size of partition
        if length % size != 0:  # if can't evenly partition, skip
            continue
        partition_counts = [Counter(text[i:i+size]) for i in range(0, length, size)]
        if all(count == partition_counts[0] for count in partition_counts[1:]):
            return True
    return False