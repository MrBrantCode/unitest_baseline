"""
QUESTION:
Write a function named `countDivisors` that takes an integer `n` as input and returns the total number of divisors of `n` that are composed only of digits. A divisor is considered to be composed only of digits if all its digits are divisors of `n`.
"""

def countDivisors(n):
    """
    Function to count the total number of digit only divisors of n
    """
    count = 0
    for i in range(1, n + 1):
        divisor = True
        num = i
        while num:
            digit = num % 10
            if digit != 0 and n % digit != 0:
                divisor = False
                break
            num = num // 10
        if divisor and n % i == 0: 
            count += 1
    return count