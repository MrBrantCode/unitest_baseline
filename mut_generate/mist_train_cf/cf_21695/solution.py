"""
QUESTION:
Write a function `find_most_common_integer(lst)` that finds the most common positive integer in a list of integers without using any built-in functions or data structures. The function should return the most common positive integer in the list, excluding any duplicates. If there are multiple integers with the same maximum frequency, return any one of them.
"""

def find_most_common_integer(lst):
    max_count = 0
    most_common = None
    
    for i in range(len(lst)):
        if lst[i] > 0:
            count = 0
            for j in range(len(lst)):
                if lst[j] == lst[i]:
                    count += 1
            if count > max_count:
                max_count = count
                most_common = lst[i]
    
    return most_common