"""
QUESTION:
Write a function `substitute_sequence(seq, sub_value)` that takes a sequence of integers `seq` and a substitute value `sub_value` as input. The function should generate a new sequence by substituting elements of `seq` with `sub_value` under the following conditions: the length of the substituted sequence should be less than the input sequence, the highest value in the substituted sequence should be more than that in the input sequence, and the highest value in the substituted sequence should match the provided `sub_value`. Return the substituted sequence that satisfies the above conditions; otherwise, return an empty list.
"""

from typing import List

def substitute_sequence(seq: List[int], sub_value: int) -> List[int]:
    if sub_value <= max(seq) or len(seq) <= 1:
        return []
    
    out1 = [sub_value if num < sub_value else num for num in seq]
    
    return out1 if len(out1) < len(seq) and max(out1) > max(seq) and max(out1) == sub_value else []