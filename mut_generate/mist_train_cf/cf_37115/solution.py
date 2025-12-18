"""
QUESTION:
Implement the `update_boids` function to update the velocities of a group of boids based on the three rules of boids flocking behavior: separation, alignment, and cohesion. The function should take in the current positions and velocities of the boids as input.

The function signature is:
```python
def update_boids(boids_positions, boids_velocities):
```
Where:
- `boids_positions` is a list of 2D positions (x, y) for each boid, with the number of boids between 3 and 50.
- `boids_velocities` is a list of 2D velocities (vx, vy) for each boid.
 
The function should return the updated list of velocities. Assume the positions and velocities are represented as lists of tuples, where each tuple contains two float values.
"""

import math

def update_boids(boids_positions, boids_velocities):
    separation_distance = 100.0
    alignment_distance = 10000.0
    cohesion_distance = 10000.0
    max_speed = 10.0
    max_rule_velocity = 0.02

    new_velocities = []

    for i in range(len(boids_positions)):
        separation = [0.0, 0.0]
        alignment = [0.0, 0.0]
        cohesion = [0.0, 0.0]

        for j in range(len(boids_positions)):
            if i != j:
                dx = boids_positions[j][0] - boids_positions[i][0]
                dy = boids_positions[j][1] - boids_positions[i][1]
                distance = math.sqrt(dx * dx + dy * dy)

                if distance < separation_distance:
                    separation[0] -= dx
                    separation[1] -= dy

                if distance < alignment_distance:
                    alignment[0] += boids_velocities[j][0]
                    alignment[1] += boids_velocities[j][1]

                if distance < cohesion_distance:
                    cohesion[0] += boids_positions[j][0]
                    cohesion[1] += boids_positions[j][1]

        new_velocity = [boids_velocities[i][0], boids_velocities[i][1]]

        if separation[0] != 0 or separation[1] != 0:
            new_velocity[0] += separation[0]
            new_velocity[1] += separation[1]

        if alignment[0] != 0 or alignment[1] != 0:
            new_velocity[0] += alignment[0] / (len(boids_positions) - 1)
            new_velocity[1] += alignment[1] / (len(boids_positions) - 1)

        if cohesion[0] != 0 or cohesion[1] != 0:
            cohesion[0] /= (len(boids_positions) - 1)
            cohesion[1] /= (len(boids_positions) - 1)
            cohesion[0] -= boids_positions[i][0]
            cohesion[1] -= boids_positions[i][1]
            new_velocity[0] += cohesion[0]
            new_velocity[1] += cohesion[1]

        speed = math.sqrt(new_velocity[0] * new_velocity[0] + new_velocity[1] * new_velocity[1])
        if speed > max_speed:
            new_velocity[0] = (new_velocity[0] / speed) * max_speed
            new_velocity[1] = (new_velocity[1] / speed) * max_speed

        new_velocities.append((new_velocity[0], new_velocity[1]))

    return new_velocities