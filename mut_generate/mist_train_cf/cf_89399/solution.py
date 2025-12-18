"""
QUESTION:
Create a function `remove_duplicates(arr)` that takes an array of integers as input, removes all duplicate elements while keeping track of the count of each unique element, and returns the unique elements in descending order based on their count. The input array should contain at least 1,000,000 elements, all of which are positive integers less than or equal to 1,000. The function should have a time complexity of O(n log n) and a space complexity of O(n).
"""

def remove_duplicates(arr):
    n = len(arr)
    
    # Sort the array in ascending order
    arr.sort()
    
    # Use two pointers to track unique elements and their counts
    unique_elements = []
    counts = []
    
    # Initialize the pointers
    i = 0
    j = 0
    
    while i < n:
        # Move the pointer j until a different element is found
        while j < n and arr[i] == arr[j]:
            j += 1
        
        # Add the unique element and its count to the lists
        unique_elements.append(arr[i])
        counts.append(j - i)
        
        # Move the pointer i to the next unique element
        i = j
    
    # Sort the unique elements and their counts in descending order based on counts
    unique_elements = [x for _, x in sorted(zip(counts, unique_elements), reverse=True)]
    counts.sort(reverse=True)
    
    return unique_elements, counts