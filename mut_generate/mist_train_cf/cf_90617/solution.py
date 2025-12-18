"""
QUESTION:
Create a function `reverse_and_get_prime_numbers` that takes a list of integers as input. Reverse the order of the list in place and then return a new list containing only the prime numbers from the reversed list. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list.
"""

import math

def reverse_and_get_prime_numbers(numbers):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        numbers[left], numbers[right] = numbers[right], numbers[left]
        left += 1
        right -= 1
    
    prime_numbers = [num for num in numbers if num > 1 and all(num % i for i in range(2, int(math.sqrt(num)) + 1))]
    
    return prime_numbers