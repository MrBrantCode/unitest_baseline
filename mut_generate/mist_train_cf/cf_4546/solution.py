"""
QUESTION:
Write a function `print_reverse(lst, index)` that takes a list `lst` and an index `index` as arguments. The function should print the elements of the list in reverse order without using any built-in functions or additional data structures, and it should have a space complexity of O(1). The function should be implemented recursively.
"""

def print_reverse(lst, index):
    if index < 0:
        return
    
    print(lst[index], end=' ')
    
    print_reverse(lst, index - 1)