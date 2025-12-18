"""
QUESTION:
Write a function `removeDuplicates` that removes duplicates from a sequence, including nested sequences, while preserving the original order of elements. The function should handle edge cases such as empty sequences and sequences with only a single element correctly. The time complexity should be O(n), where n is the length of the input sequence, and the space complexity should be O(n), assuming the worst case scenario where all elements of the input sequence are unique, including the nested sequences.
"""

from typing import Any, List, Set, Tuple

def removeDuplicates(seq: List[Any]) -> List[Any]:
    uniqueElements: List[Any] = []
    uniqueSet: Set[Any] = set()

    for element in seq:
        if isinstance(element, list):
            subList: List[Any] = []
            for subElement in element:
                if subElement not in uniqueSet:
                    subList.append(subElement)
                    uniqueSet.add(subElement)
            subTuple: Tuple[Any] = tuple(subList)
            if subTuple not in uniqueSet:
                uniqueElements.append(subList)
                uniqueSet.add(subTuple)
        else:
            if element not in uniqueSet:
                uniqueElements.append(element)
                uniqueSet.add(element)

    return uniqueElements