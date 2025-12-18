"""
QUESTION:
Implement a function named `analyze_list` that takes a list of integers as input and returns a list containing the sum, product, and maximum value of the integers. The function should also check if the list contains any prime numbers and append a corresponding string ("The list contains prime numbers" or "The list does not contain prime numbers") to the result list.
"""

import math

def analyze_list(nums):
    # Calculate the sum of the integers
    total_sum = sum(nums)
    
    # Calculate the product of the integers
    product = 1
    for num in nums:
        product *= num
    
    # Find the maximum value
    max_value = max(nums)
    
    # Check if the list contains any prime numbers
    has_prime = False
    for num in nums:
        if num > 1:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    break
            else:
                has_prime = True
        if has_prime:
            break
    
    # Create a result list
    result = [total_sum, product, max_value]
    
    # Append the appropriate string based on whether prime numbers are found or not
    if has_prime:
        result.append("The list contains prime numbers")
    else:
        result.append("The list does not contain prime numbers")
    
    return result