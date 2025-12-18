"""
QUESTION:
Implement a function `swap_and_count_operations` that takes a list and two elements as input, swaps all occurrences of the two elements in the list, and returns the number of swap operations performed along with the modified list. The function should handle lists with duplicate elements and have a time complexity of O(n) and space complexity of O(1).
"""

def swap_and_count_operations(lst, a, b):
    operations = 0
    for i in range(len(lst)):
        if lst[i] == a or lst[i] == b:
            lst[i] = b if lst[i] == a else a
            operations += 1
    return operations, lst