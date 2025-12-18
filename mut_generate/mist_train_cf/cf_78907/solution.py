"""
QUESTION:
Create a function named `filter_odd_sort_decrease` that takes an integer as input. The function should eliminate even digits from the integer, sort the remaining odd digits in descending order, and return the sorted digits along with their frequency. The input integer should not exceed 10^5.
"""

from collections import Counter

def filter_odd_sort_decrease(num):
    # Make sure number does not exceed the limit
    if num > 10**5:
        return "Number exceeds the limit"

    num_str = str(num)
    # Filter out even digits
    odd_digits = filter(lambda x: int(x) % 2 != 0, num_str)
    # Sort the digits in decreasing order
    sorted_ = sorted(odd_digits, reverse=True)

    # Calculate frequency of each digit
    freq = Counter(sorted_)

    # Return the sorted digits and their frequency
    return ''.join(sorted_), dict(freq)