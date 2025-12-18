"""
QUESTION:
Write a function `find_triplet(arr, target)` that takes an array of integers `arr` and a target integer `target` as input, and returns `True` if there exist three distinct elements in the array whose sum is equal to the target, and `False` otherwise. The array may contain duplicate numbers, but the three elements selected for the sum must be different.
"""

def find_triplet(arr, target):
    # Sort the array in non-decreasing order
    arr.sort()
    
    # Iterate through each element in the array
    for i in range(len(arr) - 2):
        # Use two pointers approach to find remaining two elements
        left = i + 1
        right = len(arr) - 1
        
        while left < right:
            # Calculate the sum of three elements
            current_sum = arr[i] + arr[left] + arr[right]
            
            # If the sum is equal to the target, return true
            if current_sum == target:
                return True
            
            # If the sum is less than the target, move the left pointer one step to the right
            elif current_sum < target:
                left += 1
            
            # If the sum is greater than the target, move the right pointer one step to the left
            else:
                right -= 1
    
    # If no valid triplet is found, return false
    return False