"""
QUESTION:
Write a function `find_largest_sum` that takes a list of integers as input and returns a tuple containing the largest sum of any three consecutive integers in the list and their corresponding start and end indices. The function should iterate through the list, calculating the sum of each consecutive set of three numbers and updating the largest sum and indices accordingly.
"""

def find_largest_sum(nums):
    largest_sum = float('-inf')
    start_index = 0
    end_index = 0
    
    for i in range(len(nums) - 2):
        current_sum = nums[i] + nums[i+1] + nums[i+2]
        
        if current_sum > largest_sum:
            largest_sum = current_sum
            start_index = i
            end_index = i+2
    
    return (largest_sum, start_index, end_index)