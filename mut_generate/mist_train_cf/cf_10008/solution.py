"""
QUESTION:
Create a function called `product_array` that takes an array of positive integers as input and returns an array where each index is the product of all the numbers except for the number at that index. The input array will not contain any negative numbers or zeros.
"""

def product_array(nums):
    result = []
    total_product = 1
    
    # Calculate the product of all numbers in the input array
    for num in nums:
        total_product *= num
    
    # Calculate the product of all numbers except the number at each index
    for num in nums:
        result.append(total_product // num)
    
    return result