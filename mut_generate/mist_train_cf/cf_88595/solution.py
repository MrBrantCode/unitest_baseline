"""
QUESTION:
Write a function named `merge_sorted_subarrays` that takes two lists of integers `ar1` and `ar2` as input. The function should merge the two lists into a single sorted list in ascending order without using any built-in sorting functions or additional data structures. The input lists may contain duplicate elements and may not be fully sorted. If one of the input lists is empty, return the other list.
"""

def merge_sorted_subarrays(ar1, ar2):
    # Check if either ar1 or ar2 is empty
    if len(ar1) == 0:
        return ar2
    if len(ar2) == 0:
        return ar1
    
    # Create an empty result array
    result = []
    
    # Compare the first elements of ar1 and ar2
    if ar1[0] <= ar2[0]:
        # Append the first element of ar1 to the result array
        result.append(ar1[0])
        # Recursively merge the remaining elements of ar1 with ar2
        result += merge_sorted_subarrays(ar1[1:], ar2)
    else:
        # Append the first element of ar2 to the result array
        result.append(ar2[0])
        # Recursively merge the remaining elements of ar2 with ar1
        result += merge_sorted_subarrays(ar1, ar2[1:])
    
    # Return the result array
    return result