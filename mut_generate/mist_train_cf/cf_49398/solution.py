"""
QUESTION:
Implement the `remove_duplicates` function, which takes a list of integers as input and returns the list with all duplicate integers removed, while preserving the original order of the remaining integers. The function must have a time complexity of O(n) and a space complexity of O(1), without using additional data structures like sets or lists. However, a solution using O(n) space complexity is acceptable if it's not possible to achieve O(1) space complexity due to the limitations of Python lists.
"""

from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = {} 
    res = []
    
    for num in numbers:
        if num not in seen: 
            seen[num] = True
            res.append(num)
    
    return res