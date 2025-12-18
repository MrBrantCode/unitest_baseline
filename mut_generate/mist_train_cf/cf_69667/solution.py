"""
QUESTION:
Create a function called `max_points` that takes in three parameters: `set_points` and `scores`, which are lists of integers representing the weights and values of items respectively, and an integer `target` representing the maximum weight limit. Using dynamic programming, the function should return the maximum possible score that can be achieved by selecting items from `set_points` without exceeding the `target` weight limit, with the option to select each item multiple times.
"""

def max_points(set_points, scores, target):
  """
  Returns the maximum possible score that can be achieved by selecting items from 
  set_points without exceeding the target weight limit.

  Parameters:
  set_points (list): A list of integers representing the weights of items.
  scores (list): A list of integers representing the values of items.
  target (int): An integer representing the maximum weight limit.

  Returns:
  int: The maximum possible score.
  """
  dp_table = [0]*(target+1)

  for capacity in range(1, target+1):
    for i in range(len(set_points)):
      if set_points[i] <= capacity:
        dp_table[capacity] = max(dp_table[capacity], dp_table[capacity - set_points[i]] + scores[i])

  return dp_table[target]