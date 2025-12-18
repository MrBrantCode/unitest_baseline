"""
QUESTION:
Write a function `car_race_collision` that takes three parameters: the number of vehicles `n`, a list of tuples `left_cars` representing the coordinates (x, t) of vehicles moving from left to right, and a list of tuples `right_cars` representing the coordinates (x, t) of vehicles moving from right to left. The function should return a list of tuples, each containing the time of a collision and the indices of the vehicles involved in the collision in the `left_cars` and `right_cars` lists. The function should return the collisions in chronological order. Assume that two vehicles collide if they reach the center at the same time.
"""

from typing import List, Tuple

def car_race_collision(n: int, left_cars: List[Tuple[float, float]], right_cars: List[Tuple[float, float]]) -> List[Tuple[float, int, int]]:
    collisions = []
    
    for i in range(n):
        left_car = left_cars[i]
        for j in range(n):
            right_car = right_cars[j]
            
            # Check if a collision occured
            if left_car[1] == right_car[1]:
                collisions.append((left_car[1], i, j))

    # Sort the collisions based on time
    collisions.sort(key=lambda x: x[0])
    
    return collisions