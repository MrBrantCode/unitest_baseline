"""
QUESTION:
Write a function called `odd_rev_concat` that takes a list of lists of arbitrary depth as input and returns a new list containing the values at odd positions in each list in reverse order, concatenated together in the same order as the original lists. The function should only use for loops, lambda functions, and iterators, and should not use recursion or any built-in functions that directly solve the problem.
"""

from typing import List, Union

def odd_rev_concat(nested_list: List[Union[int, List]]) -> List[int]:
    result = []
    stack = [(nested_list, False)]
    while stack:
        lst, is_reversed = stack.pop()
        if isinstance(lst, int):
            if not is_reversed:
                result.append(lst)
        else:
            for i, val in enumerate(lst):
                stack.append((val, not is_reversed if i % 2 == 1 else is_reversed))
    return result