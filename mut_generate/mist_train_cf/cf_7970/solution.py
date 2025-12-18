"""
QUESTION:
Write a function `remove_duplicates` that takes a list of elements as input and returns a new list containing the unique elements from the original list in their original order, without using any built-in functions or libraries. The function should have a time complexity of O(n^2) and should only use a single loop.
"""

def remove_duplicates(original_list):
    result = []
    
    for num in original_list:
        if num not in result:
            result.append(num)
    
    return result