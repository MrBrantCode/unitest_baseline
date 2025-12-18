"""
QUESTION:
Implement a function `rearrangeLadybugs` that takes in an array `ladybugs` where 0 represents an empty position and 1 represents the presence of a ladybug. The function should rearrange the ladybugs according to the following rules: 
- If a ladybug is in its correct position (i.e., at index `i` where `ladybugs[i] == 1`), it should not be moved.
- If a ladybug is not in its correct position, it should be moved to the nearest empty position to its left. If no empty position is found to the left, it should be moved to the nearest empty position to its right.

The function should return the rearranged array. The input array can contain multiple ladybugs.
"""

from typing import List

def rearrangeLadybugs(ladybugs: List[int]) -> List[int]:
    ladybugs = ladybugs[:]  # Create a copy of the input array to avoid modifying it
    for ladybugIndex in range(len(ladybugs)):
        if ladybugs[ladybugIndex] == 1:  
            continue  

        leftFound = False
        for i in range(ladybugIndex - 1, -1, -1):  
            if ladybugs[i] == 0:  
                ladybugs[i], ladybugs[ladybugIndex] = ladybugs[ladybugIndex], ladybugs[i]
                leftFound = True
                break  

        if not leftFound:  
            for j in range(ladybugIndex + 1, len(ladybugs)):  
                if ladybugs[j] == 0:  
                    ladybugs[j], ladybugs[ladybugIndex] = ladybugs[ladybugIndex], ladybugs[j]
                    break  

    return ladybugs 