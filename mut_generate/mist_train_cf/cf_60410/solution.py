"""
QUESTION:
Implement the function `car_race_collision` that takes in three parameters: an integer `n`, and two lists of tuples `left_cars` and `right_cars`, where each tuple contains a float value representing the vehicle's position and time taken to approach the epicenter. The function should return a list of tuples, where each tuple contains the time of collision, the index of the leftward-moving vehicle, and the index of the rightward-moving vehicle. The function should preserve the vehicle trajectories intact and account for the sequence and temporal frequency of collisions. The returned list of collisions should be sorted by time.
"""

from typing import List, Tuple

def car_race_collision(n: int, left_cars: List[Tuple[float, float]], right_cars: List[Tuple[float, float]]) -> List[Tuple[int, int, int]]:
    collisions = [] 
    for i in range(n):
        for j in range(n):
            # if the times for the two cars to reach the epicenter are the same
            if abs(left_cars[i][1] - right_cars[j][1]) < 1e-6: 
                collisions.append((left_cars[i][1], i, j)) 
    # return list of collisions, sorted by time
    return sorted(collisions, key = lambda x: x[0])