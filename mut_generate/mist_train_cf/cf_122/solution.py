"""
QUESTION:
Write a function `delete_and_sum(lst)` that takes a list `lst` as input and returns the sum of the remaining items after deleting all items with a value of 3. The function should handle cases where the list is empty or contains only items with a value of 3, and should have a time complexity of O(n), where n is the length of the list. Do not use built-in functions or methods that directly solve this problem.
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