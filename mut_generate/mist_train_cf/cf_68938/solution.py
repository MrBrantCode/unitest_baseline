"""
QUESTION:
Implement a function `intersperse` that takes a list of integers `numbers`, an integer `delimiter`, and optional parameters `even_positions_only` (defaulting to `False`) and `skip_first_n` (defaulting to `0`). The function should insert the `delimiter` between elements in the `numbers` list, with the option to only insert at even positions (`even_positions_only=True`) and to skip the first `n` elements (`skip_first_n=n`).
"""

from typing import List

def intersperse(numbers: List[int], delimiter: int, even_positions_only: bool = False, skip_first_n: int = 0) -> List[int]:
    if even_positions_only:
        for i in range(len(numbers) - 1, 0, -1):
            if (i+1) % 2 == 0 and i >= skip_first_n:
                numbers.insert(i, delimiter)
    else:
        for i in range(len(numbers) - 1, skip_first_n, -1):
            numbers.insert(i, delimiter)
    return numbers