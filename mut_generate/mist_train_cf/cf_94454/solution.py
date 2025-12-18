"""
QUESTION:
Implement a function named `copy_sorted_unique` that takes an array as input and returns a new array with the following properties: it is a copy of the input array, it contains only unique elements, and it is sorted in ascending order. You cannot use any built-in sorting or duplicate removal functions or methods.
"""

def copy_sorted_unique(arr):
    # Create an empty result list
    result = []
    
    # Iterate over each element in the input array
    for num in arr:
        # Check if the element is already in the result list
        if num not in result:
            # If not, add it to the result list
            result.append(num)
    
    # Sort the result list in ascending order
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]
    
    # Return the sorted and unique result list
    return result