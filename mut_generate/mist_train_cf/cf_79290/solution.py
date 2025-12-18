"""
QUESTION:
Create a function named `prod_of_primes_and_fibs` that takes a list of numbers as input. The function should calculate the product of the first ten prime numbers and the first ten Fibonacci numbers present in the list. The function should be able to handle lists containing negative numbers, floating point numbers, and complex numbers, and should return a message if the list does not contain enough prime numbers or Fibonacci numbers.
"""

def prod_of_primes_and_fibs(lst):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def is_fibonacci(n):
        x = 5 * n**2
        return x**0.5 % 1 == 0 or (x + 4)**0.5 % 1 == 0

    def prod(nums):
        result = 1
        for num in nums:
            result *= num
        return result

    primes = [x for x in lst if isinstance(x, int) and x > 0 and is_prime(x)]
    fibs = [x for x in lst if isinstance(x, int) and x > 0 and is_fibonacci(x)]
    
    if len(primes) >= 10 and len(fibs) >= 10:
        return prod(primes[:10]) * prod(fibs[:10])
    else:
        return "List does not contain enough prime numbers or Fibonacci numbers."