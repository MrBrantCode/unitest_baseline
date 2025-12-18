"""
QUESTION:
Create a function named `sum_and_count_odd_numbers` that takes an array of positive integers as input and returns a tuple containing the sum of all the odd numbers in the array and the count of odd numbers. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.
"""

def entrance(nums):
    odd_sum = 0
    odd_count = 0
    
    for num in nums:
        if num % 2 == 1:  
            odd_sum += num
            odd_count += 1
    
    return odd_sum, odd_count