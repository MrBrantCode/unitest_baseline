"""
QUESTION:
Implement a function `median` that uses the Quickselect algorithm to find the median of a list of numbers. The function `median` should call another function `quickselect_median` which then calls `quickselect` function. The `quickselect` function uses a pivot function `pivot_fn` to determine the pivot element.
"""

def median(numbers):
    def quickselect(numbers, k, pivot_fn):
        if len(numbers) == 1:
            return numbers[0]

        pivot = pivot_fn(numbers)

        lows = [el for el in numbers if el < pivot]
        highs = [el for el in numbers if el > pivot]
        pivots = [el for el in numbers if el == pivot]

        if k < len(lows):
            return quickselect(lows, k, pivot_fn)
        elif k < len(lows) + len(pivots):
            return pivots[0]
        else:
            return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)

    def quickselect_median(numbers, pivot_fn):
        if len(numbers) % 2 == 1:
            return quickselect(numbers, len(numbers) // 2, pivot_fn)
        else:
            return 0.5 * (quickselect(numbers, len(numbers) // 2 - 1, pivot_fn) +
                          quickselect(numbers, len(numbers) // 2, pivot_fn))

    return quickselect_median(numbers, pivot_fn=lambda x: x[len(x) // 2])