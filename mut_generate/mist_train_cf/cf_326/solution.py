"""
QUESTION:
Create a function named `is_prime(num)` to determine whether a given number is prime or not. The function should have a time complexity of O(sqrt(n)), where n is the input number. The function should not use any external libraries or built-in functions related to prime numbers and should return False when a number is not prime. 

Using the `is_prime(num)` function, create another function `sum_of_primes(n)` that calculates the sum of all the prime numbers from 1 to n and returns the sum along with the count of prime numbers encountered. The space complexity of the program should be O(1), excluding the input and output variables.
"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(n):
    count = 0
    sum_of_primes = 0
    for num in range(1, n+1):
        if is_prime(num):
            count += 1
            sum_of_primes += num
    return sum_of_primes, count