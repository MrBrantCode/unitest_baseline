"""
QUESTION:
Write a function `find_most_common_integer(lst)` that finds the most common positive integer in a list of integers. The function should only consider positive integers, exclude duplicates, and not use any built-in functions or data structures. The function should return the most common positive integer.
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
            if count > max_count and lst.count(lst[i]) > lst.count(most_common) if most_common is not None else True:
                max_count = count
                most_common = lst[i]
    
    return most_common