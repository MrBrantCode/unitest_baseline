"""
QUESTION:
Write a function named `remove_duplicates` that takes a list as input and returns a new list containing the unique elements from the original list, in the same order. The function should not use any built-in functions or libraries, and it should only use a single loop. The time complexity of the function should be O(n^2).
"""

def remove_duplicates(original_list):
    result = []
    
    for num in original_list:
        if num not in result:
            result.append(num)
    
    return result