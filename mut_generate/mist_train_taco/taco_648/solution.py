"""
QUESTION:
# Task
 Initially a number `1` is written on a board. It is possible to do the following operations with it:
```
multiply the number by 3;
increase the number by 5.```
Your task is to determine that using this two operations step by step, is it possible to obtain number `n`?

# Example

 For `n = 1`, the result should be `true`.
 
 `1 = 1`
 
 For `n = 2`, the result should be `false`.
 
 For `n = 3`, the result should be `true`.
 
 `1 x 3 = 3`
 
 For `n = 4`, the result should be `false`.
 
 For `n = 5`, the result should be `false`.
 
 For `n = 6`, the result should be `true`.
 
 `1 + 5 = 6`
 
 For `n = 18`, the result should be `true`.
 
 `1 + 5 = 6  --> 6 x 3 = 18`
 
 For `n = 32`, the result should be `true`.
 
 `1 x 3 x 3 x 3 = 27  --> 27 + 5 = 32`
 
 For `n = 100`, the result should be `false`.
 
 For `n = 101`, the result should be `true`.
 
 `1 + 5 + 5 + 5 ... +5 = 101`
 
# Input / Output


 - `[input]` integer n

  positive integer, n ≤ 100000


 - `[output]` a boolean value

  `true` if N can be obtained using given operations, `false` otherwise.
"""

def can_obtain_number(n):
    if n == 1:
        return True
    if n < 1:
        return False
    
    # Use a set to keep track of visited numbers to avoid infinite loops
    visited = set()
    
    # Use a queue to perform a breadth-first search (BFS)
    queue = [1]
    
    while queue:
        current = queue.pop(0)
        
        # Generate the next possible numbers
        next_numbers = [current * 3, current + 5]
        
        for next_num in next_numbers:
            if next_num == n:
                return True
            if next_num < n and next_num not in visited:
                visited.add(next_num)
                queue.append(next_num)
    
    return False