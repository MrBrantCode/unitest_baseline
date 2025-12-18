"""
QUESTION:
Implement a MedianCalculator class with the following methods: `__init__(self, numbers)` and `get_median(self)`. The `__init__` method initializes the class instance with a list of numbers. The `get_median` method returns the median of the input list, ignoring non-numeric elements and handling the case where the list is empty by returning None. The median is the middle value of a sorted list of numbers; for an odd-length list, it is the center value, and for an even-length list, it is the average of the two middle values.
"""

from typing import List, Union, Optional

def findMedian(numbers: List[Union[int, float]]) -> Optional[Union[int, float]]:
    numbers = [num for num in numbers if isinstance(num, (int, float))]
    numbers.sort()
    length = len(numbers)

    if length == 0:
        return None

    if length % 2 == 1:
        return numbers[length // 2]
    else:
        return (numbers[length // 2 - 1] + numbers[length // 2]) / 2