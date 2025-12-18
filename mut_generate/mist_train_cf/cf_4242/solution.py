"""
QUESTION:
Implement a function named bubble_sort that sorts a given list of elements in ascending order using the Bubble Sort algorithm and returns the sorted list along with the number of comparisons and swaps performed. The function should handle lists containing a mix of integers, negative integers, strings, and tuples, placing negative integers before positive integers and sorting strings and tuples in lexicographical order. The time complexity of the function should be O(n^2), where n is the length of the input list.
"""

def bubble_sort(lst):
    comparisons = 0
    swaps = 0
    n = len(lst)
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            comparisons += 1
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swaps += 1
                
    return lst, comparisons, swaps