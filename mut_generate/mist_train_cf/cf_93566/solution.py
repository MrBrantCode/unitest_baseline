"""
QUESTION:
Design a function `delete_duplicates` that takes a list of integers as input and returns a new list of tuples, where each tuple contains a unique integer from the original list and its count. The function should maintain the order of the original list, exclude duplicates, and have a time complexity of O(n), where n is the length of the input list. The function must be implemented without using any built-in Python functions or libraries.
"""

def delete_duplicates(lst):
    count_dict = {}
    result = []
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    for num in lst:
        if count_dict[num] > 0:
            result.append((num, count_dict[num]))
            count_dict[num] = 0
    
    return result