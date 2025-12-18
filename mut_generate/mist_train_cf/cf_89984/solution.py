"""
QUESTION:
Implement a function named `reverse_print` that takes a list of numbers as input and prints them in reverse order without using any loops or built-in functions for reversing the list. The function should use recursion, have a time complexity of O(n), and not modify the original list.
"""

def reverse_print(lst):
    def reverse_print_helper(index):
        if index < 0:
            return
        print(lst[index], end=' ')
        reverse_print_helper(index - 1)

    reverse_print_helper(len(lst) - 1)
    print()