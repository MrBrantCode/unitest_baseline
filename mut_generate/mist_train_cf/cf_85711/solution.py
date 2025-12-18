"""
QUESTION:
Create a function named `quick_sort` that sorts a given list of alphanumeric strings in lexicographical order. The function should take a list of strings as input and return the sorted list. The implementation should be recursive and use the Quick sort algorithm. The list may contain strings with both letters and numbers.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        items_greater = []
        items_lower = []

        for item in arr:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)
    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)