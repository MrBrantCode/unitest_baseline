"""
QUESTION:
Write a function `max_consecutive_subarrays` that finds the maximum number of consecutive subarrays in an array such that the sum of each subarray is equal to a specified number. The subarrays must have a length of at least 3. The function takes two parameters: `arr` (the input array) and `target_sum` (the specified sum).
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