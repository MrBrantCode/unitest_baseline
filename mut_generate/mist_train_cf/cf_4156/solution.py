"""
QUESTION:
Write a recursive function `move_disk` that takes four parameters: `n` (number of disks to be moved), and three tower names: `source`, `destination`, and `auxiliary`. The function should move `n` disks from `source` to `destination` following these rules:
- A disk can only be moved to a tower that is at least three positions away from its current tower.
- Disks are always moved in descending order from top to bottom.
- No larger disk is ever placed on top of a smaller disk.
- The function should not use any loops or iteration.
"""

def move_disk(n, source, destination, auxiliary):
    if n == 0:
        return
    
    move_disk(n-1, source, auxiliary, destination)
    
    print(f"Move disk {n} from tower {source} to tower {auxiliary}")
    print(f"Move disk {n} from tower {auxiliary} to tower {destination}")
    
    move_disk(n-1, auxiliary, destination, source)