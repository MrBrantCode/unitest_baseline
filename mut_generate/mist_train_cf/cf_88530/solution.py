"""
QUESTION:
Write a function named `print_reverse` that prints the elements of a given list of integers in reverse order. The function should take the list and an index as arguments, not use any built-in functions or additional data structures, and maintain a space complexity of O(1). The function should be implemented recursively.
"""

def print_reverse(lst, index):
    if index < 0:
        return
    
    print(lst[index], end=' ')
    print_reverse(lst, index - 1)