"""
QUESTION:
Design a function `indexOf7SurroundedByPrimes` that takes a string of text as input and returns the position index of the numeric character '7' if it is surrounded by prime numbers on both sides, excluding its appearance at the beginning and end of the number sequence. The function should ignore any non-numeric characters and return -1 if no such '7' character is found. The indexing is based on 0.
"""

def indexOf7SurroundedByPrimes(s):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    
    s = ''.join(i for i in s if i.isdigit())       
    if len(s) < 3:
        return -1
    
    for i in range(1, len(s) - 1):
        if s[i] == '7' and is_prime(int(s[i-1])) and is_prime(int(s[i+1])):
            return i
    return -1