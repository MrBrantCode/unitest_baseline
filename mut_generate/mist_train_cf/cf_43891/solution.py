"""
QUESTION:
Write a function called `correct_solution` that takes a non-empty list of integers as input and returns the sum of all prime numbers situated at even index locations in the list. The function should include a helper function `is_prime` that checks whether a number is prime or not. The prime check should be performed for numbers at even index locations only.
"""

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def correct_solution(lst): 
    result = 0
    for i in range(len(lst)):
        if i % 2 == 0 and is_prime(lst[i]):
            result += lst[i]
    return result