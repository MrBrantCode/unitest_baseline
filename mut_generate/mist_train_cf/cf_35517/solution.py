"""
QUESTION:
Implement a function `calculateScore(x_center, y_center, radius, x, y)` to calculate the score of a game based on the distance between the center of a target and the point where the ball hits the target. The target is divided into concentric circles with score values based on the distance from the center. The function should take the coordinates of the center (x_center, y_center), the radius of the target, and the coordinates of the point where the ball hits the target (x, y) as input and return the score as an integer. 

The scoring rules are as follows: 
- If the distance is greater than the radius, the score is 0.
- If the distance is within the radius, the score is determined by the following criteria: 
  - 10 if the distance is less than or equal to 1/5 of the radius.
  - 5 if the distance is greater than 1/5 of the radius but less than or equal to 2/5 of the radius.
  - 3 if the distance is greater than 2/5 of the radius but less than or equal to 3/5 of the radius.
  - 2 if the distance is greater than 3/5 of the radius but less than or equal to 4/5 of the radius.
  - 1 if the distance is greater than 4/5 of the radius but less than or equal to the radius.
 
The function should return the score rounded to the nearest integer.
"""

import math

def calculateScore(x_center, y_center, radius, x, y) -> int:
    distance = math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2)
    
    if distance > radius:
        return 0
    elif distance <= radius / 5:
        return 10
    elif distance <= 2 * radius / 5:
        return 5
    elif distance <= 3 * radius / 5:
        return 3
    elif distance <= 4 * radius / 5:
        return 2
    else:
        return 1