"""
QUESTION:
Write a function named remove_duplicates that takes a list of strings as input and returns a new list with all duplicates removed, maintaining the original order of elements. The function should achieve a time complexity of O(n) and a space complexity of O(n), without using built-in functions or methods that directly remove duplicates. No additional data structures should be used other than the input list itself.
"""

def remove_duplicates(lst):
    seen = {}
    unique_lst = []
    
    for elem in lst:
        if elem not in seen:
            seen[elem] = True
            unique_lst.append(elem)
    
    return unique_lst