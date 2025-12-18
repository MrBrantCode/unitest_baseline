"""
QUESTION:
Write a function `find_prime_greater_than_10` that takes a list of integers as input and returns the first prime number in the list that is greater than 10. If no such prime number exists in the list, the function should return a value indicating that. Assume that the input list contains only non-negative integers.
"""

def find_prime_greater_than_10(lst):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1): 
            if n % i == 0: 
                return False
        return True 

    for number in lst:
        if number > 10 and is_prime(number):
            return number
    return None  # return None if no prime number greater than 10 exists