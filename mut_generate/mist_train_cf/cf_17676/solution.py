"""
QUESTION:
Implement a function `hamming_distance(str1, str2)` to calculate the Hamming distance between two binary strings of any length, considering only '0' and '1' characters while ignoring any additional characters. The function should return the Hamming distance as an integer, and if the strings have different lengths, return -1 or handle it according to your preference.
"""

def hamming_distance(str1, str2):
    # Make sure the strings have the same length
    if len(str1) != len(str2):
        return -1

    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1

    return distance