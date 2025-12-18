"""
QUESTION:
Implement the `valid_transition` function to check if a transition from `tower_i` to `tower_j` is valid in the Tower of Hanoi puzzle based on the `currentState` of the towers. The `currentState` is a list of lists where each inner list represents the disks on a tower. `tower_i` and `tower_j` are integers representing the indices of the towers to move a disk from and to, respectively. The function should return a boolean value indicating whether the transition is valid according to the rules: 
- Only one disk can be moved at a time.
- Each move consists of taking the top disk from one of the stacks and placing it on top of the stack on another rod.
- No disk may be placed on top of a smaller disk.
"""

def valid_transition(currentState, tower_i, tower_j):
    if tower_i == tower_j:  
        return False

    if len(currentState[tower_i]) == 0:  
        return False

    if len(currentState[tower_j]) == 0:  
        return True

    top_disk_i = currentState[tower_i][-1]  
    top_disk_j = currentState[tower_j][-1]  

    return top_disk_i < top_disk_j  