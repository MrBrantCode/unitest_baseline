"""
QUESTION:
Write a function named `filter_and_print_sum` that takes a list of integers as input and filters out numbers that are divisible by both 3 and 5 but not by 2. The function should then check each filtered number to determine if it is a prime number, printing the result. If no numbers are found to filter, the function should print "No numbers to filter." or "No filtered numbers found." If no prime numbers are found, it should print "No prime numbers found." The function should also calculate the average of the prime numbers and print it rounded to the nearest integer. Non-integer values in the input list should be skipped.
"""

import math

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

def filter_and_print_sum(numbers):
    if len(numbers) == 0:
        print("No numbers to filter.")
        return
    
    filtered_numbers = []
    for number in numbers:
        if isinstance(number, int):
            if number % 3 == 0 and number % 5 == 0 and number % 2 != 0:
                filtered_numbers.append(number)
    
    if len(filtered_numbers) == 0:
        print("No filtered numbers found.")
        return
    
    prime_numbers = []
    prime_sum = 0
    for number in filtered_numbers:
        if is_prime(number):
            prime_numbers.append(number)
            prime_sum += number
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    
    if len(prime_numbers) == 0:
        print("No prime numbers found.")
        return
    
    average_prime = round(prime_sum / len(prime_numbers))
    print(f"The average of the prime numbers is {average_prime}.")