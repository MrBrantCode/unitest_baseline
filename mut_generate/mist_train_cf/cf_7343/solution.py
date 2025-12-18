"""
QUESTION:
You are given a list of integers. Implement the following functions:

1. `find_divisible_numbers(numbers: List[int]) -> List[int]`: Find all the numbers that are divisible by both 3 and 7.
2. `calculate_average(numbers: List[int]) -> float`: Calculate the average of the numbers.
3. `find_maximum(numbers: List[int]) -> int`: Find the maximum value among the numbers.
4. `find_minimum(numbers: List[int]) -> int`: Find the minimum value among the numbers.
5. `count_occurrences(numbers: List[int]) -> Dict[int, int]`: Determine the number of occurrences of each unique number divisible by both 3 and 7 in the list.

Constraints:
- The length of the input list can be up to 10^6.
- The values in the input list can be both positive and negative integers.
- Time Complexity Requirement: O(nlogn)
- Space Complexity Requirement: O(n)
"""

from typing import List

def entrance(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num % 21 == 0]