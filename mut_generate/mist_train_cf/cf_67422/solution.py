"""
QUESTION:
Implement the `update_points` function and a while loop control structure to regulate gameplay. The function `update_points` should take the player's current action and points as input, and update the points based on the following rules: 
- Increment points by 10 if the action is 'win'.
- Decrement points by 20 if the action is 'lose'.
- For every third 'win' action, add a bonus increment of 30 points to the player's points.

The while loop should stop running when the player's points exceed the given threshold. The initial points and threshold are given as inputs.
"""

def update_points(action, points, win_count):
    if action == 'win':
        points += 10
        win_count += 1
        if win_count == 3:
            points += 30
            win_count = 0
    else:
        points -= 20
    return points, win_count