"""
QUESTION:
Create a function `even_odd_prime_count` that takes an integer as input and returns a tuple of three integers representing the counts of even, odd, and prime digits in the integer. Consider only single-digit prime numbers (2, 3, 5, 7). The function should work for both positive and negative integers.
"""

def even_odd_prime_count(num):
    even_count = 0
    odd_count = 0
    prime_count = 0
    prime_list = [2,3,5,7] 
    for digit in str(abs(num)):
        digit = int(digit)
        if digit % 2 == 0:
            even_count += 1
        elif digit % 2 !=0:
            odd_count += 1
        if digit in prime_list:
            prime_count += 1
    return even_count, odd_count, prime_count