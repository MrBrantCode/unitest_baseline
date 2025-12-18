"""
QUESTION:
Develop a function called `solution` that accepts an array of integers as input and returns a dictionary. The function should determine if the array contains at least one positive integer, calculate the sum of all non-positive integers (negative numbers and zero), and identify all prime numbers in the array. The returned dictionary should contain three keys: `has_positive` (a boolean indicating the presence of a positive number), `sum_of_nonpositive` (the sum of non-positive integers), and `primes` (a list of prime numbers found in the array).
"""

def solution(arr):
    def is_prime(n):
        if n == 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    has_positive = False
    sum_of_nonpositive = 0
    primes = []

    for num in arr:
        if num > 0:
            has_positive = True
        elif num <= 0:
            sum_of_nonpositive += num

        if num > 1 and is_prime(num):
            primes.append(num)

    result = {
        'has_positive': has_positive, 
        'sum_of_nonpositive': sum_of_nonpositive, 
        'primes': primes
    }
    
    return result