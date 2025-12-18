"""
QUESTION:
Create a function `median` that calculates the median of a list of numbers without sorting it. The function should work with lists of both even and odd lengths, returning the middle element for odd lengths and the average of the two middle elements for even lengths.
"""

def quickselect_median(numbers):
    n = len(numbers)
    if n < 1:
            return None
    if n % 2 == 1:
            return quickselect(numbers, n//2)
    else:
            return 0.5 * (quickselect(numbers, n//2 - 1) + quickselect(numbers, n//2))

def quickselect(numbers, k):
    if len(numbers) == 1:
            return numbers[0]
    pivot = numbers[len(numbers) // 2]
    left = [x for x in numbers if x < pivot]
    middle = [x for x in numbers if x == pivot]
    right = [x for x in numbers if x > pivot]

    if k < len(left):
            return quickselect(left, k)
    elif k < len(left) + len(middle):
            return numbers[k]
    else:
            return quickselect(right, k - len(left) - len(middle))