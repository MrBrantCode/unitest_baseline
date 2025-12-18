"""
QUESTION:
Write a function `min_operations_to_target` that calculates the least number of steps needed to reach a target number starting from 0 using the arithmetic operations addition, subtraction, multiplication, and division. The division operation performs integer division, discarding the decimal part. The function should return the minimum number of operations required to reach the target.
"""

from collections import deque

def min_operations_to_target(target):
    """
    This function calculates the least number of steps needed to reach a target number 
    starting from 0 using the arithmetic operations addition, subtraction, multiplication, 
    and division. The division operation performs integer division, discarding the decimal part.

    Args:
    target (int): The target number to be reached.

    Returns:
    int: The minimum number of operations required to reach the target.
    """
    
    # Initialize the queue with the starting number 0 and its step count 0
    queue = deque([(0, 0)])
    
    # Initialize a set to store visited numbers
    visited = set([0])
    
    while queue:
        current, steps = queue.popleft()
        
        # If current number is the target, return the step count
        if current == target:
            return steps
        
        # Perform operations on current number and enqueue the results
        for next_num in [current + 1, current - 1, current * 2, current // 2]:
            if next_num not in visited:
                queue.append((next_num, steps + 1))
                visited.add(next_num)
    
    # If the target is not reachable, return -1
    return -1