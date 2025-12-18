"""
QUESTION:
Implement an iterative quicksort function in Python, called quicksort, that takes a list of integers as input, sorts the list in ascending order without using recursion or built-in sorting functions, and handles duplicate elements correctly. The function should have an average time complexity of O(n log n) and be able to handle input sizes up to 10^6 efficiently.
"""

def quicksort(lst):
    stack = []
    stack.append((0, len(lst)-1))

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = low
            pivot = lst[pivot_index]
            i = low + 1
            j = high

            while True:
                while i <= j and lst[i] <= pivot:
                    i += 1
                while i <= j and lst[j] >= pivot:
                    j -= 1
                if i <= j:
                    lst[i], lst[j] = lst[j], lst[i]
                else:
                    break

            lst[low], lst[j] = lst[j], lst[low]

            stack.append((low, j-1))
            stack.append((j+1, high))

    return lst