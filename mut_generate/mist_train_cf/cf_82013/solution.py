"""
QUESTION:
Write a function `min_turns` that takes three parameters: `deadends`, `obstacles`, and `target`. The function should return the minimum total number of turns needed to unlock the lock, given a `target` representing the unlock code. If it's impossible, return -1. 

The lock's initial state is '00000', a string representing the 5 wheels' state. The `deadends` is a list of codes that, if displayed on the lock, will cause the wheels to cease turning, making the lock unopenable. The `obstacles` is a list of codes that, if displayed on the lock, will require an additional move to proceed. 

The `deadends` and `obstacles` lists contain strings of digits only, and the `target` will not be in the `deadends` or `obstacles` lists. The length of `deadends`, `obstacles`, and `target` is 5.
"""

def min_turns(deadends, obstacles, target):
    """
    This function calculates the minimum total number of turns needed to unlock the lock.
    
    Parameters:
    deadends (list): A list of codes that, if displayed on the lock, will cause the wheels to cease turning.
    obstacles (list): A list of codes that, if displayed on the lock, will require an additional move to proceed.
    target (str): The unlock code.
    
    Returns:
    int: The minimum total number of turns needed to unlock the lock, or -1 if it's impossible.
    """
    
    # Create a set with deadends for efficient lookups
    deadends_set = set(deadends)
    
    # If the initial state is in the deadends set, return -1
    if '00000' in deadends_set:
        return -1
    
    # Create a queue for BFS and enqueue the initial state with distance 0
    queue = [('00000', 0)]
    
    # Create a set to store visited states
    visited = set('00000')
    
    # Create a set with obstacles for efficient lookups
    obstacles_set = set(obstacles)
    
    while queue:
        state, distance = queue.pop(0)
        
        # If the state is the target state, return the distance
        if state == target:
            return distance
        
        # Generate all possible next states
        for i in range(5):
            for j in [-1, 1]:
                # Calculate the new digit
                new_digit = (int(state[i]) + j) % 10
                
                # Create the new state
                new_state = state[:i] + str(new_digit) + state[i+1:]
                
                # If the new state is in the obstacles set, increment the distance
                new_distance = distance + 1 + (new_state in obstacles_set)
                
                # Check if the new state is not in the deadends set and has not been visited before
                if new_state not in deadends_set and new_state not in visited:
                    # Mark the new state as visited
                    visited.add(new_state)
                    
                    # Enqueue the new state with the new distance
                    queue.append((new_state, new_distance))
    
    # If the queue is empty, return -1 because no path is found
    return -1