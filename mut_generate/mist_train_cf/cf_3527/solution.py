"""
QUESTION:
Implement a function `count_or_sum` that takes in an array of integers, a target integer, and a count threshold integer. The function returns the target integer if it appears more than `count_threshold` times in the array. If the target integer appears less than or equal to `count_threshold` times, the function returns the sum of all the integers in the array. If the target integer does not appear in the array, the function returns None.

The function should take in a list of integers `arr` with a length between 1 and 10^5, a target integer `target`, and a count threshold integer `count_threshold` between 1 and the length of the array. The function should have the signature `def count_or_sum(arr: List[int], target: int, count_threshold: int) -> Union[int, None]`.
"""

from typing import List, Union

def count_or_sum(arr: List[int], target: int, count_threshold: int) -> Union[int, None]:
    count = arr.count(target)
    if count > count_threshold:
        return target
    elif count > 0:
        return sum(arr)
    else:
        return None