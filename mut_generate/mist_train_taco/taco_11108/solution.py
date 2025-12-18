"""
QUESTION:
# Task
N lamps are placed in a line, some are switched on and some are off. What is the smallest number of lamps that need to be switched so that on and off lamps will alternate with each other? 

You are given an array `a` of zeros and ones - `1` mean switched-on lamp and `0` means switched-off.

Your task is to find the smallest number of lamps that need to be switched.

# Example

For `a = [1, 0, 0, 1, 1, 1, 0]`, the result should be `3`.
```
a     --> 1 0 0 1 1 1 0
swith --> 0 1     0
became--> 0 1 0 1 0 1 0 ```

# Input/Output


- `[input]` integer array `a`

array of zeros and ones - initial lamp setup, 1 mean switched-on lamp and 0 means switched-off.

`2 < a.length <= 1000`


- `[output]` an integer

minimum number of switches.
"""

def min_switches_to_alternate_lamps(a):
    # Calculate the number of switches needed to make the lamps alternate starting with 0
    n_start_with_0 = sum((1 for (i, x) in enumerate(a) if x != i % 2))
    
    # Calculate the number of switches needed to make the lamps alternate starting with 1
    n_start_with_1 = sum((1 for (i, x) in enumerate(a) if x != (i + 1) % 2))
    
    # Return the minimum of the two possible switch counts
    return min(n_start_with_0, n_start_with_1)