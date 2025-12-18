"""
QUESTION:
Create a method called `countDuplicates` that takes a list of integers as input and returns the number of unique duplicate elements in the list. The input list may contain negative numbers, may be empty, and may contain duplicate elements in any order. The method should not modify the original list.
"""

def countDuplicates(lst):
    # Create a set to store unique elements
    unique = set(lst)
    
    # Create a count variable to keep track of duplicates
    count = 0
    
    # Iterate over the unique elements
    for num in unique:
        # Count the number of occurrences of each element in the original list
        occurrences = lst.count(num)
        
        # If there are more than 1 occurrence, it is a duplicate
        if occurrences > 1:
            count += 1
    
    return count