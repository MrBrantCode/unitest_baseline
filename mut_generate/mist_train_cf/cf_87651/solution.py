"""
QUESTION:
Create a function named "is_prime" that takes an integer as input and returns True if the number is prime, and False otherwise. Implement the function using only bitwise operations to check divisibility. Write a loop to print all the prime numbers between 1 and 1000 (including 1 and 1000) using the "is_prime" function.
"""

def is_prime(num):
    if num < 2:
        return False
    if num < 4:
        return True
    if num & 1 == 0:  
        return False
    if num < 9:
        return True
    if num % 3 == 0:  
        return False
    
    # Check for divisibility using prime numbers of the form 6k ± 1
    divisor = 5
    while divisor * divisor <= num:
        if num % divisor == 0 or num % (divisor + 2) == 0:
            return False
        divisor += 6
    
    return True