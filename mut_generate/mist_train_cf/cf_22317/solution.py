"""
QUESTION:
Create a function named `compute_hamming_distance` that calculates the Hamming distance between two input strings. The function should compare the strings character by character up to the length of the shorter string. If one of the strings is empty, the function should return the length of the non-empty string.
"""

def compute_hamming_distance(string1, string2):
    if len(string1) == 0:
        return len(string2)
    elif len(string2) == 0:
        return len(string1)
    
    distance = 0
    min_length = min(len(string1), len(string2))
    
    for i in range(min_length):
        if string1[i] != string2[i]:
            distance += 1
    
    # Add the difference in lengths to the distance
    distance += abs(len(string1) - len(string2))
    
    return distance