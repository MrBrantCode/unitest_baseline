"""
QUESTION:
Write a function `find_duplicates(arr)` that prints out all the duplicate elements in the input array `arr` without using any built-in functions or data structures. The function should have a time complexity of O(n) and a space complexity of O(1). The input array is a list of integers where each integer represents an index in the array.
"""

def find_duplicates(arr):
    slow = arr[0]
    fast = arr[0]
    
    # Phase 1: Find the intersection point of the two pointers
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        
        if slow == fast:
            break
    
    # Phase 2: Find the duplicate element
    slow = arr[0]
    
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return slow