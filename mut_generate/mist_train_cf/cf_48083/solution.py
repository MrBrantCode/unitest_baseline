"""
QUESTION:
Implement a function `spaceDebrisCollision(debris)` that takes an array of integers representing space debris in a row as input. The absolute value of each integer represents its size and the sign represents its direction (positive for right, negative for left). The function should return the state of the debris after all collisions, where smaller debris disintegrates when two pieces meet and same-sized debris disintegrate each other.

Constraints: `2 <= len(debris) <= 10^4` and `-1000 <= debris[i] <= 1000` and `debris[i] != 0`.
"""

def asteroidCollision(debris):
    
    stack = []
    
    for piece in debris:

        while stack and piece < 0 and 0 < stack[-1]:
            
            if stack[-1] < -piece:
                stack.pop()
                continue
                
            elif stack[-1] == -piece:
                stack.pop()
            
            break
        
        else:
            stack.append(piece)
    
    return stack