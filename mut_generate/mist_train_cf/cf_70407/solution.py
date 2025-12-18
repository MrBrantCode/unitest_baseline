"""
QUESTION:
Implement a function named `median` that calculates the median of a given list of numbers without using any built-in sorting functions. The function should be able to handle lists with both even and odd numbers of elements, duplicate elements, negative values, and large numbers.
"""

def median(numbers):
    """
    Calculate the median of a list of numbers.

    This function can handle lists with both even and odd numbers of elements,
    duplicate elements, negative values, and large numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The median of the list of numbers.
    """

    def partition(numbers, low, high):
        pivot = numbers[high]
        i = low - 1
        for j in range(low, high):
            if numbers[j] <= pivot:
                i = i + 1
                (numbers[i], numbers[j]) = (numbers[j], numbers[i])
        (numbers[i + 1], numbers[high]) = (numbers[high], numbers[i + 1])
        return i + 1

    def quick_select(l, low, high, ind):
        if low == high:
            return l[low]
        pi = partition(l, low, high)
        if ind == pi:
            return l[pi]
        elif ind < pi:
            return quick_select(l, low, pi - 1, ind)
        else:
            return quick_select(l, pi + 1, high, ind)

    if not numbers:
        return None

    length = len(numbers)
    if length % 2 != 0:
        return float(quick_select(numbers, 0, length - 1, length // 2))
    else:
        return (quick_select(numbers, 0, length - 1, length // 2 - 1) +
                quick_select(numbers, 0, length - 1, length // 2)) / 2.0