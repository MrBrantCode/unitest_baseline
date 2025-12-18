"""
QUESTION:
Write a function called `count_target_occurrences` that takes a list of integers `lst` and a target integer `target` as parameters, and returns the number of times the target integer appears in the list. The list is guaranteed to have between 100 and 1000 elements, and the target integer is guaranteed to be within the range of -1000 to 1000. If the list is empty, return an error message.
"""

def count_target_occurrences(lst, target):
    if not lst:
        return "Error: The list is empty."
    
    count = 0
    for num in lst:
        if num == target:
            count += 1
    
    return count