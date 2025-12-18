"""
QUESTION:
Find the second highest prime number in a list of integers, excluding any prime numbers that are divisible by 5. The function should have a time complexity of O(n) and not use any built-in sorting or mathematical functions. Define the function as `find_second_highest_prime(numbers)`.
"""

def find_second_highest_prime(numbers):
    highest_prime = 0
    second_highest_prime = 0

    for num in numbers:
        if num % 5 == 0:  
            continue

        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            if num > highest_prime:
                second_highest_prime = highest_prime
                highest_prime = num
            elif num > second_highest_prime and num != highest_prime:
                second_highest_prime = num

    return second_highest_prime