"""
QUESTION:
Create a function named `is_prime` to check if a number is prime, and a main program that prints the FizzBuzz series up to the 1000th term, where each term must be a prime number greater than 100 and divisible by 7. The FizzBuzz rules are as follows: print "Fizz" if the term count is divisible by 3, print "Buzz" if the term count is divisible by 5, and print "FizzBuzz" if the term count is divisible by both 3 and 5; otherwise, print the term count.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True