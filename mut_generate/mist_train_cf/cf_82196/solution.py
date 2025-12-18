"""
QUESTION:
Write a function named `nearest_armstrong_number(n)` that takes an integer `n` as input and returns the closest Armstrong number. An Armstrong number is an n-digit number that is equal to the sum of its digits each raised to the power of n. If the input number `n` is already an Armstrong number, the function should return `n`. Otherwise, it should return the closest Armstrong number, whether higher or lower than `n`.
"""

def nearest_armstrong_number(n):
    def is_armstrong(num):
        return num == sum(int(digit)**len(str(num)) for digit in str(num))
        
    if is_armstrong(n):
        return n
    else:
        lower = upper = n
        while True:
            if is_armstrong(lower):
                return lower
            if is_armstrong(upper):
                return upper
            lower -= 1
            upper += 1 