"""
QUESTION:
Design a function named `count_duplicates` to delete duplicates from a list while keeping track of the count of each duplicate element. The function should return a new list with the unique elements from the original list, along with their respective counts. The function should maintain the order of the original list while removing duplicates and store the count of each duplicate element as a tuple in the new list. Implement the function without using any built-in Python functions or libraries and achieve a time complexity of O(n), where n is the length of the input list. The input list can contain duplicate elements and negative numbers.
"""

def entrance(lst):
    count_dict = {}
    unique_list = []

    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num in lst:
        if count_dict[num] > 0:
            unique_list.append((num, count_dict[num]))
            count_dict[num] = 0

    return unique_list