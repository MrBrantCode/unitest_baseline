"""
QUESTION:
Calculate the quantity of uniform subsequences in a given character sequence s, considering all its constituents are identical and a subsequence is a continuous series of characters present within the character sequence, and return the result modulo 10^9 + 7.

The function name should be `numSub(s)`, where `s` is a string composed of lowercase alphabets. The length of `s` is between 1 and 10^5.
"""

def numSub(s):
    MOD = 10**9 + 7
    prev_count = [0]*26
    current_char_previous_count = 0
    result = 0
    for c in s:
        temp = current_char_previous_count
        current_char_previous_count = prev_count[ord(c) - ord('a')]
        prev_count[ord(c) - ord('a')] = (current_char_previous_count + result + 1)%MOD
        result = (result + current_char_previous_count + 1)%MOD
    return result