"""
QUESTION:
Write a function `delete_and_sum` that takes a list of integers as input, removes all items with a value of 3, and returns the sum of the remaining items. The function should handle cases where the input list is empty or contains only items with a value of 3. The time complexity of the solution should be O(n), where n is the length of the list, and it should not use any built-in functions or methods that directly solve this problem.
"""

def delete_and_sum(mylist):
    total_sum = 0
    i = 0
    while i < len(mylist):
        if mylist[i] == 3:
            del mylist[i]
        else:
            total_sum += mylist[i]
            i += 1
    return total_sum