"""
QUESTION:
Write a function named `verify_seven` that takes a string of alphanumeric characters as input and returns the position index of the digit '7' if it is surrounded by prime numbers and not at the start or end of the numeric part of the string. If no such '7' is found, the function should return -1. The function should disregard any non-decimal characters in the input string.
"""

def verify_seven(string):
    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        sqr = int(n**0.5) + 1
        for divisor in range(3, sqr, 2):
            if n % divisor == 0:
                return False
        return True

    string = ''.join(c for c in string if c.isdigit())
    len_string = len(string)

    for i in range(1, len_string - 1):
        if (string[i] == '7' and 
            is_prime(int(string[i-1])) and 
            is_prime(int(string[i+1]))):
            return i
    return -1