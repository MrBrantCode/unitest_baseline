"""
QUESTION:
Write a function `is_subset(A, B)` that determines if array B is a subset of array A, considering duplicate elements. The function should return True if all elements in B are present in A with at least the same frequency, and False otherwise. The time complexity of the function should be O(n), where n is the length of B.
"""

def is_subset(A, B):
    count = {}
    
    # Count the elements in A
    for num in A:
        count[num] = count.get(num, 0) + 1
    
    # Check if all elements in B are present in A
    for num in B:
        if num not in count or count[num] <= 0:
            return False
        count[num] -= 1
    
    return True