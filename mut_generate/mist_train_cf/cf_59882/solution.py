"""
QUESTION:
Design a function `least_freq_complex_numbers` that takes a list of unique complex numbers and two optional boolean variables `return_sorted` and `ascending` as input. The function should return the complex number(s) with the least frequency in the list. If multiple complex numbers have the same least frequency, return all of them. 

The function should support two return types: 
- If `return_sorted` is False (default), return the complex numbers in the order they first appear in the list.
- If `return_sorted` is True, return the complex numbers sorted in ascending order based on their real parts, and if the real parts are equal, compare their imaginary parts. The `ascending` variable (default is False) can be used to sort in descending order.

The function should have a time complexity of O(n log n) or better.
"""

from collections import Counter
from typing import List

def least_freq_complex_numbers(cn: List[complex], return_sorted: bool = False, ascending: bool = False) -> List[complex]:
    # Create a dictionary with the frequency count of complex numbers
    freq_dict = Counter(cn)

    # Find the least frequency
    min_freq = min(freq_dict.values())

    # Extract complex numbers that have this frequency
    least_freq_cn = [key for key, value in freq_dict.items() if value == min_freq]

    # If sorted flag is True return them sorted ascending/descending
    if return_sorted:
        return sorted(least_freq_cn, key=lambda x: (x.real, x.imag), reverse=not ascending)
    else:
        # If sorted is False return in the order they were encountered
        return sorted(least_freq_cn, key=lambda x: cn.index(x))