"""
QUESTION:
Find the position index of the digit '7' in a string of alphanumeric characters, excluding its appearance at the beginning and end of the numeric sequence, and only if it is nestled between prime numbers on either side. If the '7' digit is not found or not encapsulated by prime numbers, return -1. Non-digit characters should be ignored. The function should be named find_seven and take a string s as input.
"""

def entance(s):
    def prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    s = ''.join(filter(str.isdigit, s))
    if len(s) > 2:
        for i in range(1, len(s) - 1):
            if s[i] == '7' and prime(int(s[i-1])) and prime(int(s[i+1])):
                return i
    return -1