"""
QUESTION:
Implement a function `reverse_print` that takes a list of numbers as input, prints the numbers in reverse order without using a loop, and does not modify the original list. The solution must use recursion and have a time complexity of O(n), where n is the number of elements in the list.
"""

def reverse_print(lst):
    def helper(index):
        if index < 0:
            return
        print(lst[index], end=' ')
        helper(index - 1)
    helper(len(lst) - 1)
    print()