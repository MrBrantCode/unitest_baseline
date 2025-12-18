"""
QUESTION:
Write a function `reverse_and_get_prime_numbers` that takes a list of numbers as input, reverses the list, and returns a new list containing only the prime numbers from the reversed list. The function should have a time complexity of O(n), where n is the length of the input list, and a space complexity of O(n), where n is the maximum number of prime numbers in the input list.
"""

import math

def reverse_and_get_prime_numbers(numbers):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1
    
    prime_numbers = [num for num in numbers if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)) and num > 1]
    
    return prime_numbers