"""
QUESTION:
Write a function `is_perfect_number` that takes a positive integer `num` as input and returns a boolean value indicating whether the number is perfect or not. A number is said to be a perfect number if the sum of its proper divisors is equal to itself. The input number will not exceed 10^18. The function should have a time complexity of O(sqrt(n)), where n is the input number.
"""

import math

def is_perfect_number(num):
    if num <= 1:
        return False
    
    # Initialize the sum of divisors
    div_sum = 1
    
    # Iterate from 2 to the square root of the number
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            # Add the divisor to the sum
            div_sum += i
            
            # If the divisor is not equal to the square root of the number, add the other factor
            if i != num // i:
                div_sum += num // i
                
    # Check if the sum of divisors is equal to the number
    return div_sum == num