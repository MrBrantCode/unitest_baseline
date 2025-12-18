"""
QUESTION:
Implement a function `find_elements` that takes in a list of lists `lists` and an integer `x`, and returns a list of elements that appear exactly `x` times across all the lists. The function should consider all elements from all lists, not just unique elements within each list.
"""

from typing import List

def find_elements(lists: List[List[int]], x: int) -> List[int]:
    all_elements = [element for lst in lists for element in lst]
    return [element for element in set(all_elements) if all_elements.count(element) == x]