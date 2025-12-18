"""
QUESTION:
Write a function `hamming_distance(s1, s2)` that calculates the Hamming distance between two binary strings `s1` and `s2`. The Hamming distance is the number of positions at which the corresponding symbols are different. The function should be able to handle strings of length up to 10^6 efficiently. The input strings `s1` and `s2` are guaranteed to be of equal length.
"""

def hamming_distance(s1, s2):
    distance = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            distance += 1
    return distance