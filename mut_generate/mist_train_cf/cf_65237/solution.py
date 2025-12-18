"""
QUESTION:
Write a function `find_min(lst)` that takes a list of integers as input and returns the smallest number in the list along with its index positions. If the list contains multiple instances of the smallest number, the function should return all index positions. Do not use built-in functions like `min()` or `index()`.
"""

def find_min(lst):
    min_num = lst[0]
    min_index = [0]  
    for i in range(1, len(lst)):
        if lst[i] < min_num:
            min_num = lst[i]
            min_index = [i] 
        elif lst[i] == min_num:
            min_index.append(i)
    return min_num, min_index