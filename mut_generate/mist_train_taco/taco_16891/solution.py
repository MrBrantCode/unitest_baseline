"""
QUESTION:
Baby is getting his frst tooth. This means more sleepless nights, but with the fun of feeling round his gums and trying to guess which will be first out! 

Probably best have a sweepstake with your friends - because you have the best chance of knowing. You can feel the gums and see where the raised bits are - most raised, most likely tooth to come through first!

Given an array of numbers (t) to represent baby's gums, you need to return the index of the lump that is most pronounced. 

The most pronounced lump is the one that has the biggest differential to its surrounding values. e.g.:

```
[1, 2, 4] = 2

index 0 has a differential of -1 to its right (it is lower so the figure is negative)

index 1 has a differential of +1 to its left, and -2 to its right. Total is -1.

index 2 has a differential of +2 to its left, and nothing to its right, 
```

If there is no distinct highest value (more than one occurence of the largest differential), return -1.
"""

def find_most_pronounced_lump(gums):
    # Extend the list to handle edge cases
    extended_gums = [gums[0]] + gums + [gums[-1]]
    
    # Calculate the differential for each index
    differentials = [
        extended_gums[i + 1] * 2 - extended_gums[i] - extended_gums[i + 2]
        for i in range(len(gums))
    ]
    
    # Find the maximum differential
    max_differential = max(differentials)
    
    # Return the index of the maximum differential if it is unique
    if differentials.count(max_differential) == 1:
        return differentials.index(max_differential)
    else:
        return -1