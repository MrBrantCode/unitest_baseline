"""
QUESTION:
Write a function `count_prime_numbers` that takes an array of integers as input and returns the count of prime numbers in the array. The function should use a nested loop structure to check for prime numbers and should have a time complexity of O(n^2), where n is the length of the array. The function should not use any built-in functions or libraries for prime number generation or checking.
"""

def count_prime_numbers(arr):
    count = 0
    for num in arr:
        if num > 1:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
    return count