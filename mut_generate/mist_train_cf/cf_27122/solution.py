"""
QUESTION:
Implement a function `canCross(stones: List[int]) -> bool` that determines whether a frog can cross a river by jumping on stones. The function takes a list of integers representing the positions of the stones in the river, where the frog starts at the first stone and can jump to another stone if the distance is within a certain range. The function should return `True` if the frog can reach the last stone, and `False` otherwise.
"""

from typing import List

def canCross(stones: List[int]) -> bool:
    stone_set = set(stones)
    jumps = {stone: set() for stone in stones}
    jumps[0].add(0)
    
    for stone in stones:
        for jump in jumps[stone]:
            for next_jump in range(jump - 1, jump + 2):
                if next_jump > 0 and stone + next_jump in stone_set:
                    jumps[stone + next_jump].add(next_jump)
    
    return bool(jumps[stones[-1]])