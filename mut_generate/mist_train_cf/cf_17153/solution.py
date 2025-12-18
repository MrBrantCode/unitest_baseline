"""
QUESTION:
Write a Python function `normalize_list` that takes a list of numbers as input and returns the list normalized so that the sum of the numbers is 10. The function should handle both positive and negative numbers, and should not modify the input list if its sum is already 10. If the sum is less than 10, the function should distribute the remaining value evenly among the elements, and if the sum is greater than 10, the function should proportionally reduce the values of the elements.
"""

def normalized_list(arr):
    # Calculate the sum of the given list
    arr_sum = sum(arr)
    
    # Check if the sum is already 10
    if arr_sum == 10:
        return arr
    
    # Check if the sum is less than 10
    if arr_sum < 10:
        # Calculate the remaining value to distribute
        remaining_value = 10 - arr_sum
        
        # Calculate the increment for each element
        increment = remaining_value / len(arr)
        
        # Normalize the list by adding the increment to each element
        normalized_list = [num + increment for num in arr]
    
    # Check if the sum is greater than 10
    if arr_sum > 10:
        # Calculate the scaling factor to reduce the values proportionally
        scaling_factor = 10 / arr_sum
        
        # Normalize the list by multiplying each element with the scaling factor
        normalized_list = [num * scaling_factor for num in arr]
    
    return normalized_list