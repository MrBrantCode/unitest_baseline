"""
QUESTION:
Write a function `filter_list(lst)` that takes a list of integers as input, filters the even numbers that are at non-prime indices, divisible by 7, and have a prime number immediately following it in the list, and returns the filtered list.
"""

def filter_list(lst): 
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return [lst[i] for i in range(len(lst) - 1) if not is_prime(i) and lst[i] % 2 == 0 and lst[i] % 7 == 0 and is_prime(lst[i+1])]