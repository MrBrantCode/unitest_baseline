"""
QUESTION:
Given a string, implement the function `count_subsegments` that returns the total count of uninterrupted sub-segments present in the string, where a sub-segment is considered valid only if it contains at least one vowel and its length is greater than 2.
"""

def count_subsegments(string):
    vowels = set("AEIOUaeiou")
    n = len(string)

    res, consonant_pointer, vowel_pointer = 0, 0, 0

    for i in range(0, n, 1):
        if (string[i] not in vowels):
            consonant_pointer += 1
            vowel_pointer = 0

        else:
            vowel_pointer += 1
            res += consonant_pointer

    return res