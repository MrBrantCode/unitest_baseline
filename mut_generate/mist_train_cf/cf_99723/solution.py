"""
QUESTION:
Create a function `find_primes` that takes a list of integers as input, returns a new list containing only prime numbers from the input list, and sorts them in ascending order. The function should exclude non-prime numbers, including 1 and any numbers less than 1.
"""

def find_primes(input_list):
    """
    Returns a new list containing only prime numbers within the input list, sorted in ascending order.
    """
    primes = []
    for num in input_list:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    primes.sort()
    return primes