"""
QUESTION:
Write a function called 'sums' that takes an integer 'n' as input and returns a dictionary containing three values: 

- the sum of all positive integers from 0 to 'n', 
- the sum of squares of every positive integer in this range, 
- and the sum of all prime numbers in this range. 

If 'n' is not a positive integer, the function should return an error message.
"""

def sums(n):
    def is_prime(num):
        if num == 1 or num == 0:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    if type(n) != int or n < 0:
        return {"Error": "Input number is not a positive integer"}
  
    sum_ints = (n * (n + 1)) // 2
    sum_squares = (n*(n + 1)*(2*n + 1)) // 6
    sum_primes = sum([x for x in range(2, n+1) if is_prime(x)])
  
    return {"sum_ints": sum_ints, "sum_squares": sum_squares, "sum_primes": sum_primes}