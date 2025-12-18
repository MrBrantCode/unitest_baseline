"""
QUESTION:
Create a function `nth_number` that takes an integer `n`, an unsorted list of numbers, and a boolean flag `smallest` as input. Without using any built-in sorting methods, return the `n`th smallest number if `smallest` is `True` or the `n`th largest number if `smallest` is `False`. The value of `n` is 1-based.
"""

def nth_number(n, numbers, smallest=True):
    # Sorting the list using selection sort
    for i in range(len(numbers)):
        # find min value in remaining unsorted array
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[min_index] > numbers[j]:
                min_index = j
        # Swap min value with first element of unsorted array
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    # Return nth smallest/largest number based on the flag
    if smallest:
        return numbers[n-1]
    else:
        return numbers[-n]