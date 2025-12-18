"""
QUESTION:
Write a function named `advanced_median` that takes a list of integers and/or decimals (positive or negative) and an optional multiplier as input. The function should calculate the median of the list without sorting it or using any library functions. If the multiplier is provided, apply it to each element in the list before calculating the median. The function should be able to handle lists of both odd and even lengths. The function should return the calculated median.
"""

def advanced_median(l: list, multiplier: float =1.0):
    def partition(lst, low, high): 
        pivot = lst[high]
        i = low - 1

        for j in range(low, high):
            if lst[j] <= pivot:
                i = i + 1
                lst[i], lst[j] = lst[j], lst[i]

        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        return i + 1

    def quick_select(lst, k):
        if len(lst) == 1:
            return lst[0]

        pi = partition(lst, 0, len(lst) - 1)
        if k < pi:
            return quick_select(lst[:pi], k)
        elif k > pi:
            return quick_select(lst[pi + 1:], k - pi - 1)
        else:
            return lst[pi]

    l = [element * multiplier for element in l] # Apply multiplier
    if len(l) % 2 == 0: # If there are an even number of elements
        return (quick_select(l, len(l) // 2 - 1) + quick_select(l, len(l) // 2)) / 2.0
    else: # If there are odd number of elements
        return quick_select(l, len(l) // 2)