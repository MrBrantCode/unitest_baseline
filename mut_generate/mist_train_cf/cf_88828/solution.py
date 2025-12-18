"""
QUESTION:
Create a function named `modify_list` that takes a list of strings as input. The function should remove all strings with a length less than three and any strings that contain numbers. The modified list should then be sorted in reverse alphabetical order, and any duplicate strings should be removed. Implement a custom sorting algorithm and remove duplicates without using built-in Python methods or functions such as `sort()`, `reverse()`, or `set()`. The function should return the modified list.
"""

def modify_list(lst):
    # Remove strings with length less than three
    lst = [s for s in lst if len(s) >= 3]
    
    # Remove strings that contain numbers
    lst = [s for s in lst if not any(c.isdigit() for c in s)]
    
    # Sort the list in reverse alphabetical order
    lst = reverse_sort(lst)
    
    # Remove duplicate strings
    lst = remove_duplicates(lst)
    
    return lst

def reverse_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def remove_duplicates(lst):
    new_lst = []
    for s in lst:
        if s not in new_lst:
            new_lst.append(s)
    return new_lst