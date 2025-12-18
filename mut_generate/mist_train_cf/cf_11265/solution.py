"""
QUESTION:
Write a function named `max_consecutive_subarrays` that takes an array of integers and a target sum as input. The function should return the maximum number of consecutive subarrays of length 3 or more in the array that have a sum equal to the target sum.
"""

def max_consecutive_subarrays(arr, target_sum):
    count = 0
    max_count = 0

    # Iterate through each element in the array
    for i in range(len(arr)):
        current_sum = 0
        
        # Check if there are at least 3 elements remaining in the array
        if i + 2 < len(arr):
            # Calculate the sum of the next 3 elements
            current_sum = arr[i] + arr[i+1] + arr[i+2]
            
            # If the sum is equal to the target sum, increment the count
            if current_sum == target_sum:
                count += 1
                max_count = max(max_count, count)
            else:
                # If the sum is not equal to the target sum, reset the count
                count = 0
    
    return max_count