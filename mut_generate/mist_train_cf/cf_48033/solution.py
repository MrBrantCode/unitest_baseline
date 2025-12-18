"""
QUESTION:
Implement the `get_positive_and_sort` function and its nested function `swap_elements` to sort non-negative integers from a given list in ascending order without using the built-in Python `sort()` and `sorted()` functions. Ensure the function efficiently handles large lists with optimized time complexity and space efficiency. If the input list contains only negative integers, return an empty list.
"""

def get_positive_and_sort(l: list):
    def swap_elements(n: list, index1: int, index2: int) -> None:
        """
        Swap two elements in the list n at positions index1 and index2.
        """
        n[index1], n[index2] = n[index2], n[index1]

    non_negative = [num for num in l if num >= 0]
    for i in range(len(non_negative)):
        for j in range(len(non_negative) - 1):
            if non_negative[j] > non_negative[j + 1]:
                swap_elements(non_negative, j, j + 1)
    return non_negative