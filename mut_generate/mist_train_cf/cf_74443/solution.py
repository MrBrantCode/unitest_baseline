"""
QUESTION:
Write a function `isOneBitCharacter(bits)` that takes a list of bits as input and returns `True` if the last character must be a one-bit character and `False` otherwise. The input list will always end with a zero and can be decoded into valid characters. Note that `1 <= len(bits) <= 1000` and `bits[i]` is always `0` or `1`.
"""

def isOneBitCharacter(bits):
    i = len(bits) - 2
    while i >= 0 and bits[i] > 0:
        i -= 1
    return (len(bits) - i) % 2 == 0