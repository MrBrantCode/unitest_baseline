"""
QUESTION:
Write a function `find_unique_subsequence(input1, input2)` that takes two strings `input1` and `input2` as input and returns two strings representing the minimal distinctive subsequences present uniquely in each string. The function should consider a character as distinctive if it is present in one string but not in the other. Note that the order of characters in the distinctive subsequences may not be preserved.
"""

def find_unique_subsequence(input1, input2):
    seq1 = ''
    seq2 = ''
    for char in input1:
        if char not in input2:
            seq1 += char
    for char2 in input2:
        if char2 not in input1:
            seq2 += char2
    return seq1, seq2