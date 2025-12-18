"""
QUESTION:
Write a function named `isSelfCrossing` that takes an array of integers `distance` as input and returns `true` if the trajectory intersects itself and `false` otherwise. The trajectory starts at (0,0) and moves `distance[0]` meters north, `distance[1]` meters west, `distance[2]` meters south, `distance[3]` meters east, and so on, with direction changing counter-clockwise. The length of `distance` is between 1 and 500, and each element in `distance` is between 1 and 500.
"""

def isSelfCrossing(distance):
    padding = [0, 0, 0]
    distance = padding + distance
    for i in range(3, len(distance)):
        # Fourth line crosses first line
        if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
            return True
        # Fifth line meets first line
        if i >= 4 and distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]:
            return True
        # Sixth line crosses first line
        if i >= 5 and distance[i-2] >= distance[i-4] and distance[i] + distance[i-4] >= distance[i-2] and distance[i-1] + distance[i-5] >= distance[i-3] and distance[i-1] <= distance[i-3]:
            return True

    return False