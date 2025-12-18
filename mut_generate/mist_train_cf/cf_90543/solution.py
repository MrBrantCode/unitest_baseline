"""
QUESTION:
Write a function called `filter_and_print_sum` that takes a list of numbers as input. The function should filter the numbers that are divisible by both 3 and 5 but not by 2, and store them in a new list. It should then print the sum of the filtered numbers. If the input list is empty, the function should print "No numbers to filter." If the filtered list is empty, it should print "No filtered numbers found." The function should also check if each filtered number is a prime number, print a message indicating whether it is prime or not, and calculate the average of the prime numbers. If there are no prime numbers, it should print "No prime numbers found." The function should handle cases where the input list contains non-integer values by skipping them. The average of the prime numbers should be rounded to the nearest integer.
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