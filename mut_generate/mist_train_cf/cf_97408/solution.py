"""
QUESTION:
Create a function called `doubleAndFilterPrimes` that takes an array of integers as input and returns an array of integers. The function should double each non-negative number in the input array and check if the doubled number is prime. If the doubled number is prime, it should be included in the output array. The function should ignore any negative numbers in the input array.
"""

import math

def doubleAndFilterPrimes(nums):
    result = []
    
    for num in nums:
        if num >= 0:
            doubled_num = num * 2
            is_prime = True
            
            if doubled_num <= 1:
                is_prime = False
            else:
                for i in range(2, int(math.sqrt(doubled_num)) + 1):
                    if doubled_num % i == 0:
                        is_prime = False
                        break
            
            if is_prime:
                result.append(doubled_num)
    
    return result