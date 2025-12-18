"""
QUESTION:
Write a function named `advanced_concurrent_collision_detector` that takes three parameters: `n` as the number of automobiles in each lane, `left_lane_autos` as a list of tuples representing the start and end points of automobiles in the left lane, and `right_lane_autos` as a list of tuples representing the start and end points of automobiles in the right lane. The function should return a list of tuples, where each tuple contains the index of the collided cars in the left and right lanes and their overlapping distance. Assume that the start point of any car is less than its end point and the cars move in the positive direction.
"""

from typing import List, Tuple

def advanced_concurrent_collision_detector(n: int, left_lane_autos: List[Tuple[float, float]], right_lane_autos: List[Tuple[float, float]]) -> List[Tuple[int, int, float, float]]:
    """ Detects the concurrent collisions between cars in both lanes.
    Returns a list of tuples where each tuple represents a collision.
    The first two elements are the index of the collided cars in left and right lanes and the other two elements are the overlapping distance.

    :param n: Number of automobiles in each lane
    :param left_lane_autos: List of tuples indicating the start and end points of automobiles in left lane
    :param right_lane_autos: List of tuples indicating the start and end points of automobiles in right lane
    :return: A list of tuples indicating the collided automobiles and their overlapping distance
    """
    collisions = []
    for i in range(n):
        for j in range(n):
            if left_lane_autos[i][0] < right_lane_autos[j][1] and left_lane_autos[i][1] > right_lane_autos[j][0]:  # Check if ranges of left and right cars overlap
                overlap_start = max(right_lane_autos[j][0], left_lane_autos[i][0])
                overlap_end = min(right_lane_autos[j][1], left_lane_autos[i][1])
                collisions.append((i, j, overlap_start, overlap_end))
    return collisions