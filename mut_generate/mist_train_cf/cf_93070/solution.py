"""
QUESTION:
Write a function `find_max_product(numbers)` that takes a list of integers as input and returns the maximum product of three numbers in the list, with the condition that the product must include at least one positive number and one negative number. The function should have a time complexity of O(n), where n is the length of the list.
"""

def find_max_product(numbers):
    max1 = max2 = max3 = float('-inf')
    min1 = float('inf')
    
    for num in numbers:
        if num >= max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num >= max2:
            max3 = max2
            max2 = num
        elif num >= max3:
            max3 = num
        
        if num <= min1:
            min1 = num
    
    return max(max1 * max2 * max3, max1 * min1 * max3)