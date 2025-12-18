"""
QUESTION:
Create a function `get_positive_and_sort` that returns a list of positive numbers from the input list in ascending order. The function should also include a custom classification algorithm in a separate function named `swap_elements`. The `swap_elements` function should swap two elements in a list without using built-in functions like `sort()` or `sorted()`. The `get_positive_and_sort` function should have a time complexity of O(n^2) or better and should not use built-in sorting functions.
"""

def get_positive_and_sort(l: list):
    def swap_elements(n: list, index1: int, index2: int):
        n[index1], n[index2] = n[index2], n[index1]

    positive_integers = [num for num in l if num > 0]
    
    for i in range(len(positive_integers)):
        for j in range(len(positive_integers) - 1):
            if positive_integers[j] > positive_integers[j + 1]:
                swap_elements(positive_integers, j, j + 1)
    
    return positive_integers