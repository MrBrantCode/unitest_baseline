"""
QUESTION:
Implement a function `trapped_water_volume` that calculates the total volume of water that can be trapped between a series of connected vertical pillars, represented by an array of non-negative integers. The function should take in the array of pillar heights and return the total volume of water that can be trapped. The pillars are uniformly spaced. 

The function should have the following signature: 
```python
def trapped_water_volume(pillar_heights: List[int]) -> int:
```
"""

from typing import List

def trapped_water_volume(pillar_heights: List[int]) -> int:
    n = len(pillar_heights)
    if n < 3:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = pillar_heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], pillar_heights[i])

    right_max[n-1] = pillar_heights[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], pillar_heights[i])

    water_volume = 0
    for i in range(n):
        water_volume += max(0, min(left_max[i], right_max[i]) - pillar_heights[i])

    return water_volume