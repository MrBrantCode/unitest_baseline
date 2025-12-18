"""
QUESTION:
Implement a function `shiftingLetters(S, shifts)` that takes a string `S` of lowercase letters and an integer array `shifts` as input. The function should return the resultant string after applying a series of shifts to `S`, where for each `shifts[i] = x`, the first `i+1` letters of `S` are shifted `x` times. The shift of a letter is defined as the subsequent letter in the alphabet, with 'z' wrapping around to become 'a'. The length of `S` and `shifts` is between 1 and 20000, and each element in `shifts` is between 0 and 10^9.
"""

def shiftingLetters(S, shifts):
    totalShifts = sum(shifts)
    result = []
    for i,shift in enumerate(shifts):
        # Calculate the new character using modulus operation
        newChar = chr((ord(S[i]) - 97 + (totalShifts - (len(shifts) - i - 1) * shift) % 26) % 26 + 97)
        result.append(newChar)
    return ''.join(result)