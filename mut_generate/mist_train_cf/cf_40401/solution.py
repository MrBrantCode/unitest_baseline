"""
QUESTION:
Implement a function `reorder_axes` that reorders the axes of a multi-dimensional array based on the provided rules. The function takes three parameters: `reduce_split_axis_list`, `reduce_leveled_axes`, and `num_reduce_axis_parts`. If the length of `reduce_leveled_axes` is greater than or equal to 1, the function should reorder the axes such that the inner part is placed as the inner-most axes. The function should return the reordered axes as a list.
"""

from typing import List, Tuple

def reorder_axes(reduce_split_axis_list: List[int], reduce_leveled_axes: List[Tuple[int, int]], num_reduce_axis_parts: int) -> List[int]:
    if len(reduce_leveled_axes) >= 1:
        # GPU specific reorder choice
        # put the inner part as inner-most axes
        inner_axes = [axis for axis, level in reduce_leveled_axes if level == min([level for _, level in reduce_leveled_axes])]
        outer_axes = [axis for axis in reduce_split_axis_list if axis not in inner_axes]
        return inner_axes + outer_axes
    else:
        return reduce_split_axis_list