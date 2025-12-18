"""
QUESTION:
Write a function `sort_strings` that takes a list of strings as input and returns a new list of strings where all strings have an uppercase first letter and are sorted in descending order based on the length of each string. If there are strings with the same length, sort them alphabetically. The function should not use any built-in sorting functions, should not modify the original list, and should have a time complexity no worse than O(n^2).
"""

def sort_strings(lst):
    n = len(lst)
    # Initialize new list to copy the input list and store capitalized strings
    new_lst = [x.capitalize() for x in lst]
    
    # Perform selection sort algorithm
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if len(new_lst[j]) > len(new_lst[min_idx]):
                min_idx = j
            elif len(new_lst[j]) == len(new_lst[min_idx]) and new_lst[j] < new_lst[min_idx]:
                min_idx = j
        new_lst[i], new_lst[min_idx] = new_lst[min_idx], new_lst[i]
    
    return new_lst