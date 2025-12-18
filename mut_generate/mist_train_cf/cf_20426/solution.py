"""
QUESTION:
Write a function named `bubble_sort_unique` that sorts a list of integers in ascending order using the Bubble Sort algorithm. The function should check if the list has at least 5 elements and contains only unique integers, and if not, it should print an error message and return the original list. The algorithm should be optimized to minimize the number of comparisons made during the sorting process.
"""

def bubble_sort_unique(lst):
    if len(lst) < 5:
        print("List must have at least 5 elements.")
        return lst
    
    # Check for duplicates
    if len(set(lst)) != len(lst):
        print("List must contain only unique integers.")
        return lst
    
    n = len(lst)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        
        if not swapped:
            break
    
    return lst