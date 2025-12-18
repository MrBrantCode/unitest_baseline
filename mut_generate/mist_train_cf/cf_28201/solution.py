"""
QUESTION:
Given a list of segments, each represented by a tuple of three integers: start, end, and color, write a function `total_color_sum(segments: List[Tuple[int, int, int]]) -> int` to calculate the total sum of colors for all the non-overlapping colored regions.

Constraints:
- 1 <= segments.length <= 2 * 10^4
- segments[i].length == 3
- 1 <= starti < endi <= 10^5
- 1 <= colori <= 10^9
- Each colori is distinct.
"""

from typing import List, Tuple

def entrance(segments: List[Tuple[int, int, int]]) -> int:
    segments.sort(key=lambda x: x[1])  
    total_sum = 0
    prev_end = 0
    
    for start, end, color in segments:
        if start >= prev_end:  
            total_sum += color
            prev_end = end
    
    return total_sum