"""
QUESTION:
# Task
 Given a `sequence` of integers, check whether it is possible to obtain a strictly increasing sequence by erasing no more than one element from it.

# Example

 For `sequence = [1, 3, 2, 1]`, the output should be `false`;
 
 For `sequence = [1, 3, 2]`, the output should be `true`.

# Input/Output


 - `[input]` integer array `sequence`

    Constraints: `2 ≤ sequence.length ≤ 1000, -10000 ≤ sequence[i] ≤ 10000.`


 - `[output]` a boolean value

    `true` if it is possible, `false` otherwise.
"""

def can_be_strictly_increasing(sequence):
    save = -float('inf')
    first = True
    
    for i, x in enumerate(sequence):
        if x > save:
            save = x
        elif first:
            if i == 1 or x > sequence[i - 2]:
                save = x
            first = False
        else:
            return False
    
    return True