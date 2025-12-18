"""
QUESTION:
Create a function called `find_second_largest` that accepts an array of numbers. Implement the function to return the second largest number in the array without using any built-in sorting or maximum/minimum finding functions or methods. The function should have a time complexity of O(n) and a space complexity of O(1). If the array has less than two distinct elements, the function should return None.
"""

def entrance(nums):
    if len(nums) < 2:
        return None
    
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    if second_largest == float('-inf'):
        return None
    
    return second_largest