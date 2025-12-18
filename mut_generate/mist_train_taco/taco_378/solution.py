"""
QUESTION:
In Manhattan, roads run where the x or y coordinate is an integer. Both Sunuke-kun's house and Sumeke-kun's house are on the road, and the straight line distance (Euclidean distance) is just d. Find the maximum value that can be considered as the shortest distance when traveling along the road from Sunuke-kun's house to Sumek-kun's house.

Constraints

* 0 <d ≤ 10
* d is given up to exactly three decimal places

Input


d


Output

Print the answer on one line. If the absolute error or relative error is 10-9 or less, the answer is judged to be correct.

Examples

Input

1.000


Output

2.000000000000


Input

2.345


Output

3.316330803765
"""

def calculate_max_road_distance(d: float) -> float:
    """
    Calculate the maximum value that can be considered as the shortest distance
    when traveling along the road from Sunuke-kun's house to Sumeke-kun's house.

    Parameters:
    d (float): The Euclidean distance between Sunuke-kun's house and Sumeke-kun's house.

    Returns:
    float: The maximum road distance.
    """
    return max(2 ** 0.5 * d, int(d) + 1)