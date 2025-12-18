"""
QUESTION:
Implement a function `function_name` that accepts four parameters: `a` of type `int`, `b` of type `str`, `c` of type `List[int]`, and `d` of type `Optional[str]`. The function should return either a `str` or an `int` value based on the value of `d`. Use type hinting to specify the expected types of the parameters and the return value.
"""

from typing import List, Union, Optional

def function_name(a: int, b: str, c: List[int], d: Optional[str]) -> Union[str, int]:
    if d is not None:
        return a + len(c) + len(d)
    else:
        return b