"""
QUESTION:
Find the speed of the car's outbound journey to City B, given the distances from City B to City C and the total times for the journey from City A to City C.

Implement a function `find_speeds(distances: List[int], total_times: List[int]) -> List[float]`, where:
- distances: A list of integers, where each integer denotes the different distance from City B to City C. (1 ≤ distances.length ≤ 10⁴)
- total_times: A list of integers, where each integer denotes the total time the car took to travel from City A to City C corresponding to the distance in the distances list. (1 ≤ total_times.length = distances.length ≤ 10⁴)

The function should return a list of floating point numbers (rounded to two decimal places), each of which represents the speed of the car on its outbound journey to City B for each distance.
"""

from typing import List

def entance(distances: List[int], total_times: List[int]) -> List[float]:
    routes = list(zip(distances, total_times))
    speeds = []
    for x, T in routes:
        s = (9 * T) / (300 + 10 * x / 9)
        speeds.append(round(s, 2))
    return speeds