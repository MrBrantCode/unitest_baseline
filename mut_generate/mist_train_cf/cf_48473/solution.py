"""
QUESTION:
Write a function `generate_list(n)` that generates a list of tuples containing prime numbers between 1 and `n` and their cubes. The function should return the list of tuples. 

Restrictions: 
- The input `n` is a positive integer.
- The output list should be ordered based on the prime numbers.
- The time complexity of the function should be optimized to at least O(n^2).
"""

def generate_list(n):
    def is_prime(num):
        if num == 1:
            return False
        elif num == 2:
            return True
        else:
            for i in range(2, num):
                if num % i == 0:
                    return False
            return True

    def cube(num):
        return num**3

    lst = []
    for i in range(2, n+1):
        if is_prime(i):
            lst.append((i, cube(i)))
    return lst