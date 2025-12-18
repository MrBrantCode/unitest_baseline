"""
QUESTION:
Write a function named `hamming_distance` that calculates the Hamming distance between two binary strings. The input strings may contain additional characters other than '0' and '1' and may be up to 10^6 in length. The function should compare each corresponding pair of characters in the two strings, count the number of positions where they differ, and return this count as the Hamming distance. If the input strings have different lengths, the function should return -1.
"""

def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return -1

    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1

    return distance