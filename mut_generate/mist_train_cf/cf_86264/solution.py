"""
QUESTION:
Write a function called `delete_and_sum` that takes a list of integers as input, deletes all items with a value of 3, and returns the sum of the remaining items. The function should handle cases where the list is empty or contains only items with a value of 3. The time complexity of the solution should be O(n), where n is the length of the list, and no built-in functions or methods that directly solve the problem (such as `filter()` or list comprehension) can be used.
"""

def delete_and_sum(lst):
    if len(lst) == 0 or all(item == 3 for item in lst):
        return 0
    
    total = 0
    i = 0
    while i < len(lst):
        if lst[i] == 3:
            del lst[i]
        else:
            total += lst[i]
            i += 1
    
    return total