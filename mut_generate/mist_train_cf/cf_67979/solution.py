"""
QUESTION:
Develop a function named `find_indices` that takes two parameters: a list of integers (`nums`) and a target integer (`target`). The function should return a list of indices where `target` appears in `nums`. If `target` does not appear, return an empty list. The function must be optimized to run efficiently for large inputs of up to 10^6 items.
"""

def find_indices(nums, target):
    indices = [i for i, x in enumerate(nums) if x == target]
    return indices