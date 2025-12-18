"""
QUESTION:
Design a function named `delete_duplicates` that takes a list of integers as input and returns a new list with the unique elements from the original list, along with their respective counts. The function should maintain the order of the original list while removing duplicates, and the count of each duplicate element should be stored as a tuple in the new list, where the first element of the tuple is the duplicate element and the second element is its count. The implementation should have a time complexity of O(n), where n is the length of the input list, and should not use any built-in Python functions or libraries.
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