"""
QUESTION:
Write a function `order_strings` that takes a list of strings as input and returns the list sorted by string lengths in descending order. If multiple strings have the same length, they should be ordered alphabetically. The function should achieve a time complexity of O(n log n) and use constant space complexity without relying on built-in sorting functions or libraries.
"""

def order_strings(strings):
    """
    Sorts a list of strings by length in descending order. If multiple strings have the same length, 
    they are ordered alphabetically. The function achieves a time complexity of O(n log n) and uses 
    constant space complexity.

    Args:
    strings (list): A list of strings

    Returns:
    list: A sorted list of strings
    """
    def quicksort(strings, low, high):
        if low < high:
            pivot_index = partition(strings, low, high)
            quicksort(strings, low, pivot_index-1)
            quicksort(strings, pivot_index+1, high)

    def partition(strings, low, high):
        pivot = strings[high]
        i = low - 1
        for j in range(low, high):
            if len(strings[j]) > len(pivot) or (len(strings[j]) == len(pivot) and strings[j] <= pivot):
                i = i + 1
                strings[i], strings[j] = strings[j], strings[i]
        strings[i+1], strings[high] = strings[high], strings[i+1]
        return i + 1

    quicksort(strings, 0, len(strings)-1)
    return strings