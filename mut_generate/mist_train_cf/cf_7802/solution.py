"""
QUESTION:
Write a function `compute_hamming_distance(string1, string2)` that calculates the Hamming distance between two strings. The Hamming distance is the number of positions at which the corresponding characters are different. If the strings have different lengths, the Hamming distance should only be computed up to the length of the shorter string. If one of the strings is empty, the Hamming distance should be equal to the length of the non-empty string.
"""

def compute_hamming_distance(string1, string2):
    if len(string1) == 0:
        return len(string2)
    elif len(string2) == 0:
        return len(string1)
    
    distance = 0
    for i in range(min(len(string1), len(string2))):
        if string1[i] != string2[i]:
            distance += 1
    
    return distance + abs(len(string1) - len(string2))