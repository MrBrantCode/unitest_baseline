"""
QUESTION:
Write a function `zigzagInterleave(arr1, arr2)` that takes two sorted arrays `arr1` and `arr2` as input, and returns a new array where the largest number from `arr1` is paired with the smallest number from `arr2`, and vice versa. The remaining numbers should follow the same rule alternately. If one array is longer than the other, append the remaining numbers from the longer array according to their order in the array.
"""

def zigzagInterleave(arr1, arr2):
    # Sorts the arrays
    arr1.sort()
    arr2.sort()

    # Reverse the first array to make it largest to smallest
    arr1 = arr1[::-1]

    # Initiates the result list
    result = []

    # Loop through both arrays
    for i in range(min(len(arr1),len(arr2))):
        # Appends the largest from arr1 and smallest from arr2 alternately
        result.append(arr1[i])
        result.append(arr2[i])
    
    # If arr1 is longer, remaining numbers are appended from largest to smallest
    if len(arr1) > len(arr2):
        for i in range(len(arr2), len(arr1)):
            result.append(arr1[i])
    
    # If arr2 is longer, remaining numbers are appended from smallest to largest
    if len(arr1) < len(arr2):
        for i in range(len(arr1), len(arr2)):
            result.append(arr2[i])
    
    # Returns the final result
    return result