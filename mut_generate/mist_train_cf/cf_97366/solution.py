"""
QUESTION:
Write a function called `is_sorted_unique` that checks if a given list of integers is sorted in ascending order and contains no duplicate values. The list has a length between 1 and 10^6 and contains values between -10^6 and 10^6. The function should have a time complexity of less than O(n^2) and a space complexity of less than O(n).
"""

def is_sorted_unique(lst):
    # Check if the list is empty or has only one element
    if len(lst) < 2:
        return True
    
    # Iterate through the list and check if each element is less than the next
    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:
            return False
    
    # Check for duplicate values
    seen = set()
    for num in lst:
        if num in seen:
            return False
        seen.add(num)
    
    return True