"""
QUESTION:
Write a function called `find_second_largest` that takes an array of numbers as input and returns the second largest number without using any built-in sorting or maximum/minimum finding functions or methods. The function must have a time complexity of O(n) and a space complexity of O(1). If the input array has fewer than two distinct elements, the function should return None.
"""

def find_second_largest(nums):
    # Check if the input array is empty or has only one element
    if len(nums) < 2:
        return None
    
    # Initialize two variables to keep track of the largest and second largest numbers
    largest = float('-inf')
    second_largest = float('-inf')
    
    # Iterate through the array
    for num in nums:
        # If the current number is larger than the largest number, update both variables accordingly
        if num > largest:
            second_largest = largest
            largest = num
        # If the current number is smaller than the largest but larger than the second largest, update the second largest
        elif num > second_largest and num != largest:
            second_largest = num
    
    # If the second largest variable was not updated, it means there is no second largest number
    if second_largest == float('-inf'):
        return None
    
    return second_largest