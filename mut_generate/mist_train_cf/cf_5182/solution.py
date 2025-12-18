"""
QUESTION:
Create a function called `modify_list` that takes a list of strings as input. The function should remove any strings with a length less than 3 and any strings that contain numbers. The remaining strings should be sorted in reverse alphabetical order, and any duplicates should be removed. The function must not use built-in Python methods or functions such as `sort()`, `reverse()`, or `set()` for sorting and removing duplicates. Instead, implement a custom sorting algorithm and remove duplicates manually. The function should return the modified list.
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