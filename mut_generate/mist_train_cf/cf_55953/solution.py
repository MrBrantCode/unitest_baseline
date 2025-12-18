"""
QUESTION:
Write a function named `median` that calculates the median of a list of numbers without sorting the list, handling both even and odd number of elements. The function should not rearrange the original list.
"""

def partition(l, low, high):
    pivot = l[high]
    i = low - 1 
    for j in range(low, high):
        if l[j] <= pivot:
            i += 1
            l[i], l[j] = l[j], l[i]
            
    l[i+1], l[high] = l[high], l[i+1]
    return i + 1

def quickselect(l, k):
    if len(l) == 1:
        return l[0]
    pivot_index = partition(l, 0, len(l) - 1)
    if pivot_index == k:
        return l[pivot_index]
    elif pivot_index > k:
        return quickselect(l[:pivot_index], k)
    else:
        return quickselect(l[pivot_index + 1:], k - pivot_index - 1)

def median(numbers):
    n = len(numbers)
    mid1, mid2 = quickselect(numbers, n // 2), None
    if n % 2 == 0:
        mid2 = quickselect(numbers, n // 2 - 1)
        return (mid1 + mid2) / 2
    else:
        return mid1