"""
QUESTION:
Create a function named common(l1: list, l2: list) that returns a sorted list of unique integer elements common to both input lists. The function should not use Python's native list functionalities. The function must handle variable-length lists and lists containing float numbers by rounding them to the nearest integer. It should also efficiently manage negative numbers and ensure correct sorting.
"""

def common(l1: list, l2: list):
    # Initialize list for common elements
    common_elements = []

    # Round all elements to the nearest integer
    l1 = list(map(round, l1))
    l2 = list(map(round, l2))

    # Iterate over l1 to find common elements
    for i in l1:
        if i in l2 and i not in common_elements:
            common_elements.append(i)

    # Function for exclusive sorting and duplicate removal
    def sort_and_remove_duplicates(lst):
        # Implementation of bubble sort
        for i in range(len(lst)):
            for j in range(len(lst) - 1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]

        # Duplicate removal
        i = 0
        while i < len(lst)-1:
            if lst[i] == lst[i+1]:
                lst.pop(i)
            else:
                i += 1
        
        return lst

    # Return the sorted list of unique common elements
    return sort_and_remove_duplicates(common_elements)