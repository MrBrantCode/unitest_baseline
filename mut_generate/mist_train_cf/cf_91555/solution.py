"""
QUESTION:
Write a function named `hamming_distance` that calculates the Hamming distance of two binary strings of equal length, which is the number of positions at which the corresponding symbols are different. The function should take two binary strings `s1` and `s2` as input and return the Hamming distance. The input strings can be up to 10^6 characters long.
"""

def hamming_distance(s1, s2):
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance