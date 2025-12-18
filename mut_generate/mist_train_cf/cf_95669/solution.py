"""
QUESTION:
Write a function named `merge_sorted_subarrays` that takes two sorted subarrays `ar1` and `ar2` as input and returns a single sorted array containing all elements from both input arrays. The function should not use any built-in sorting functions or additional data structures. It should handle arrays with duplicate elements and arrays that are not fully sorted.
"""

def merge_sorted_subarrays(ar1, ar2):
    # Step 1: Check if either ar1 or ar2 is empty
    if len(ar1) == 0:
        return ar2
    if len(ar2) == 0:
        return ar1
    
    # Step 2: Create an empty result array
    result = []
    
    # Step 3: Compare the first elements of ar1 and ar2
    if ar1[0] <= ar2[0]:
        # Step 4: Append the first element of ar1 to result and recursively merge the remaining elements
        result.append(ar1[0])
        result += merge_sorted_subarrays(ar1[1:], ar2)
    else:
        # Step 5: Append the first element of ar2 to result and recursively merge the remaining elements
        result.append(ar2[0])
        result += merge_sorted_subarrays(ar1, ar2[1:])
    
    # Step 8: Return the result array
    return result