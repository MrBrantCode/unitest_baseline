"""
QUESTION:
Create a function `filter_sort` that takes a list of integers as input, and returns a list containing only the odd numbers from the original list in descending order, with no duplicates. The function should not use any built-in functions or methods for sorting or removing duplicates, and should not use any additional data structures.
"""

def filter_sort(nums):
    # Step 1: Filter odd numbers
    odds = []
    for num in nums:
        if num % 2 != 0:
            odds.append(num)
    
    # Step 2: Sort in descending order (using bubble sort algorithm)
    n = len(odds)
    for i in range(n-1):
        for j in range(n-i-1):
            if odds[j] < odds[j+1]:
                odds[j], odds[j+1] = odds[j+1], odds[j]
    
    # Step 3: Remove duplicates
    i = 0
    while i < len(odds)-1:
        if odds[i] == odds[i+1]:
            odds.pop(i+1)
        else:
            i += 1
    
    return odds