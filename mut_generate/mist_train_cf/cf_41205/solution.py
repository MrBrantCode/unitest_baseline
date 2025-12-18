"""
QUESTION:
Write a function `convert(s)` that takes a JSON string `s` as input, where `s` represents a dictionary with integer keys and lists of integers as values. The dictionary represents points in a 2D plane, with each key corresponding to the y-coordinate and the list of integers containing the x-coordinates of points at that y-coordinate. The function should return the minimum x-coordinate and the minimum y-coordinate as a tuple `(minx, miny)`.

Function signature: `def convert(s: str) -> Tuple[int, int]`
"""

import json
from typing import Tuple

def convert(s: str) -> Tuple[int, int]:
    d = json.loads(s)[0]
    minx = min(min(d[y]) for y in d)
    miny = min(map(int, d.keys()))
    return minx, miny