"""
QUESTION:
Find the kth smallest number in a list of length n. Implement a function named `quick_select` that takes as input a list `lst`, integers `low` and `high` representing the range of the list to consider, and an integer `k` representing the kth smallest number to find. The function should return the kth smallest number in the list. The list may contain duplicate elements. Do not use any built-in sort function.
"""

def quick_select(lst, low, high, k):
    def partition(lst, low, high):
        i = (low - 1)         # index of smaller element
        pivot = lst[high]     # pivot

        for j in range(low, high):
            # If current element is smaller than or
            # equal to pivot
            if lst[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        return i + 1

    if 1 <= k <= high - low + 1:
        index = partition(lst, low, high)
        if index - low == k-1:
            return lst[index]
        if index - low > k-1:
            return quick_select(lst, low, index - 1, k)
        return quick_select(lst, index + 1, high, k - index + low - 1)
    return float('inf')