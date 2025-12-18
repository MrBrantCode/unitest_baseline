"""
QUESTION:
Create a Python function named `get_permutations` that takes a list of unique numerical elements `arr` and an integer `n` as inputs. The function should return the first `n` unique permutations of the input list. If `n` exceeds the total number of possible permutations (`len(arr)!`), the function should return a message indicating that not enough unique permutations are available.
"""

import itertools

def get_permutations(arr, n):
    all_perms = list(itertools.permutations(arr))
    
    # Validate if we can return the required number of permutations
    if len(all_perms) < n:
        return "Not enough unique permutations available"

    return all_perms[:n]