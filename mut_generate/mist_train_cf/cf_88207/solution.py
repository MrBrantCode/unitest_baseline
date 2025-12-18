"""
QUESTION:
Write a function named `find_kth_smallest_element` that takes two parameters: `lst` (a list containing integers and/or non-integer elements) and `k` (the position of the desired element). The function should find the kth smallest element in the list. If the list is empty, return "Error: The list is empty." If k is greater than the length of the list, return "Error: k is greater than the length of the list." The function should be optimized for time complexity and should not use any built-in sorting functions.
"""

def find_kth_smallest_element(lst, k):
    if not lst:
        return "Error: The list is empty."
    if k > len(lst):
        return "Error: k is greater than the length of the list."
        
    # Function to partition the list
    def partition(lst, low, high):
        pivot = lst[high]
        i = low - 1
        for j in range(low, high):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        return i + 1

    # Function to find the kth smallest element
    def find_kth(lst, low, high, k):
        pivot_index = partition(lst, low, high)
        if pivot_index == k - 1:
            return lst[pivot_index]
        elif pivot_index < k - 1:
            return find_kth(lst, pivot_index + 1, high, k)
        else:
            return find_kth(lst, low, pivot_index - 1, k)
    
    return find_kth(lst, 0, len(lst) - 1, k)