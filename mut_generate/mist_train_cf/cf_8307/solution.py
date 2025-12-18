"""
QUESTION:
Create a function named `check_strings` that takes two strings as input and returns a boolean value. The function should check the following conditions: 
1. The lengths of both strings must be prime numbers.
2. Neither string should contain any palindromic substrings of length greater than 2.
3. The strings must have the same length and contain no duplicate characters.
If all conditions are met, return True; otherwise, return False.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def check_strings(string1, string2):
    length1 = len(string1)
    length2 = len(string2)
    
    if not is_prime(length1) or not is_prime(length2):
        return False
    
    for i in range(length1 - 2):
        for j in range(i + 2, length1):
            substring = string1[i:j+1]
            if substring == substring[::-1]:
                return False
    
    for i in range(length2 - 2):
        for j in range(i + 2, length2):
            substring = string2[i:j+1]
            if substring == substring[::-1]:
                return False
    
    if length1 != length2:
        return False
    
    if len(set(string1)) != length1 or len(set(string2)) != length2:
        return False
    
    return True