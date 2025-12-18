"""
QUESTION:
Implement a function named `calculate_mean(arr)` that takes an array of integers as input and returns the mean of the array, rounded to 2 decimal places. The function should not use any built-in functions or libraries that directly calculate the mean. Instead, it should manually sum up all elements in the array and divide by the total number of elements. The function should also handle edge cases, such as an empty array or an array containing only negative numbers, and return 0 in these cases.
"""

def calculate_mean(arr):
    total_sum = 0
    count = 0
    
    for num in arr:
        total_sum += num
        count += 1
    
    if count == 0 or total_sum < 0:
        return 0
    
    mean = total_sum / count
    
    # Round the mean to 2 decimal places
    decimal_place = 2
    rounded_mean = int(mean * (10 ** decimal_place) + 0.5) / (10 ** decimal_place)
    
    return rounded_mean