"""
QUESTION:
Create a function `median_and_mode` that takes a list of integers as input and returns a tuple containing the median and mode of the list. The function should be able to handle lists of even or odd length, negative elements, and duplicates. The function should not use built-in sort or median/mode calculation functions, but it can use other built-in functions such as `len()`. However, for simplicity and clarity, a solution using built-in sort function is acceptable.
"""

def median_and_mode(l: list):
    n = len(l)
    frequency = {}
    mode = None
    max_count = 0
    for number in l:
        # Count frequencies
        if number not in frequency:
            frequency[number] = 1
        else:
            frequency[number] += 1
        # Update mode
        if frequency[number] > max_count:
            max_count = frequency[number]
            mode = number
    # Get mode
    if max_count == 1:
        mode = None
    # Prepare list, sort values
    l = sorted([value for value in l])
    # Get median
    if n % 2 == 0:
        median = (l[n//2 - 1] + l[n//2]) / 2
    else:
        median = l[n//2]
        
    return (median, mode)