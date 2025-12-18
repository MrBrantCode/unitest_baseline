"""
QUESTION:
Design a function called `binary_transform` that takes three binary strings as input: `init_str`, `target1`, and `target2`. The function should determine if `init_str` can be transformed into both `target1` and `target2` by flipping exactly one bit for each transformation. The function should return two sets of transformations and their sequence, if they exist, or return a negative response if either or both transformations are not possible. The function should assume that the transformations can be made in any order. The input strings are guaranteed to only contain binary digits (0 and 1). The output should be in the format `{'Target1': 'Flip bit at position X', 'Target2': 'Flip bit at position Y'}`, where X and Y are the positions (1-indexed) of the bits that need to be flipped.
"""

def binary_transform(init_str, target1, target2):
    # Check if strings lengths match
    if not (len(init_str) == len(target1) == len(target2)):
        return "Input strings are not the same length."

    # Check if only one bit needs flipping to achieve target strings
    diff1 = [i for i in range(len(init_str)) if init_str[i] != target1[i]]
    diff2 = [i for i in range(len(init_str)) if init_str[i] != target2[i]]
  
    if len(diff1) > 1 or len(diff2) > 1:
        return "More than one bit needs flipping."

    # Check if the two targets are reachable from the initial string
    reachable = set(init_str) == set(target1) == set(target2)
    if not reachable:
        return "Targets aren't reachable from initial string."

    return {'Target1': f'Flip bit at position {diff1[0] + 1}', 'Target2': f'Flip bit at position {diff2[0] + 1}'}