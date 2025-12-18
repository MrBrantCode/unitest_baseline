"""
QUESTION:
Write a function `get_prime_numbers` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should not modify the original list and should not include 1 in the output list, as 1 is not considered a prime number.
"""

def get_prime_numbers(numbers):
    prime_numbers = []
    
    for num in numbers:
        if num > 1:
            for i in range(2, int(num/2) + 1):
                if (num % i) == 0:
                    break
            else:
                prime_numbers.append(num)
    
    return prime_numbers