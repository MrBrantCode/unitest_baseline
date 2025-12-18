"""
QUESTION:
Given an array of strings, group all strings that belong to the same shifting sequence and return the groups and the total number of unique shifting sequences. Two strings are in the same shifting sequence if the sequence of differences between successive characters is the same. The input array `strings` has a length between 1 and 200, each string has a length between 1 and 50, and consists of lowercase English letters. Write a function `groupStrings(strings)` to solve this problem.
"""

def groupStrings(strings):
    hashmap = {}
    for s in strings:
        key = tuple((ord(s[i]) - ord(s[i - 1])) % 26 for i in range(1, len(s)))
        if key not in hashmap:
            hashmap[key] = [s]
        else:
            hashmap[key].append(s)
    return list(hashmap.values()), len(hashmap)