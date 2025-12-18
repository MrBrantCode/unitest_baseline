"""
QUESTION:
Write a function named `longestCommonSuffix` that takes a list of strings `strs` as input and returns the longest common suffix among all strings in the list. The function should return an empty string if the input list is empty.
"""

def longestCommonSuffix(strs):
    if not strs:
        return ""

    shortest_str = min(strs, key=len)

    for i in range(len(shortest_str)):
        for other in strs:
            if shortest_str[::-1][i:] != other[::-1][:i+1]:
                return shortest_str[::-1][:i][::-1]

    return shortest_str