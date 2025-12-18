"""
QUESTION:
Create a function `isSubsequence` that takes two arrays of integers `arr1` and `arr2` as parameters and returns a boolean value. The function should return true if `arr2` is a subsequence of `arr1`, meaning that the elements of `arr2` can be derived from `arr1` by deleting some or no elements without changing the order of the remaining elements. The integers in the arrays can range from -1000 to 1000. The function should have a time complexity of O(n), where n is the length of the longer array, and a space complexity of O(1).
"""

def isSubsequence(arr1, arr2):
    # Initialize two pointers to track the position in the arrays
    pointer1 = 0
    pointer2 = 0
    
    # Loop until we reach the end of one of the arrays
    while pointer1 < len(arr1) and pointer2 < len(arr2):
        # If the current elements match, move both pointers forward
        if arr1[pointer1] == arr2[pointer2]:
            pointer1 += 1
            pointer2 += 1
        # If the current elements don't match, move only the pointer in the first array
        else:
            pointer1 += 1
    
    # Check if we reached the end of the second array
    return pointer2 == len(arr2)