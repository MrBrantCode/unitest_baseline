"""
QUESTION:
Implement a function named `isStrobogrammatic` that takes a string `num` as input and returns `True` if `num` is a strobogrammatic number and a palindrome, and `False` otherwise. A strobogrammatic number is a number that looks the same when rotated `180` degrees, and a palindrome number is a number that remains the same when its digits are reversed. The input string `num` consists of only digits, does not contain any leading zeros except for zero itself, and its length is between `1` and `50` (inclusive).
"""

def isStrobogrammatic(num):
    strobogrammatic = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    rotated = ''
    for n in reversed(num):
        if n not in strobogrammatic:
            return False
        rotated += strobogrammatic[n]
        
    return num == rotated