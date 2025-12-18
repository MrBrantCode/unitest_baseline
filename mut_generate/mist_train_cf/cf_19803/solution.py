"""
QUESTION:
Create a function called `last_k_unique_elements` that takes an array `arr` and a positive integer `K` as input. The function should return the last K unique elements of the array in the order they appear from left to right. The function should have a time complexity of O(K) and a space complexity of O(K).
"""

def last_k_unique_elements(arr, K):
    frequency = {}
    unique_elements = []
    
    # Iterate over the array in reverse order
    for i in range(len(arr)-1, -1, -1):
        if arr[i] not in frequency:
            unique_elements.append(arr[i])
            frequency[arr[i]] = 1
            
            # Break the loop if we have found K unique elements
            if len(unique_elements) == K:
                break
    
    # Return the last K unique elements
    return unique_elements[::-1]