"""
QUESTION:
Implement a function `sum_and_average` that takes an array of integers and returns the sum and average of its elements without using built-in sum or average functions. The array can have any length, contain both positive and negative integers, and have duplicate elements. The function must achieve a time complexity of O(n) and space complexity of O(1).
"""

def sum_and_average(arr):
    # Initialize sum and count variables
    total_sum = 0
    count = 0
    
    # Iterate through each element in the array
    for num in arr:
        # Add the current element to the sum
        total_sum += num
        # Increment the count
        count += 1
    
    # Calculate the average by dividing the sum by the count
    average = total_sum / count
    
    # Return the sum and average as a tuple
    return total_sum, average