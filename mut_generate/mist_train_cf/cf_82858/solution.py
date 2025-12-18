"""
QUESTION:
Write a function `track_duplicates(numbers)` that removes duplicates from a list of integers and maintains the original order of elements. It should also identify duplicates and return both the list of non-duplicate elements and the list of duplicate elements. The function should achieve O(n) time complexity, but due to the problem's nature, O(1) space complexity cannot be achieved without some form of storage.
"""

from typing import List, Tuple

def track_duplicates(numbers: List[int]) -> Tuple[List[int], List[int]]:
    count = {}
    no_duplicates = []
    duplicates = []
    for num in numbers:
        if num not in count:
            count[num] = 0
            no_duplicates.append(num)  
        count[num] += 1
    
    for num, times in count.items():
        if times > 1:
            duplicates.append(num)  
    return no_duplicates, duplicates