"""
QUESTION:
# Task
 Some people are standing in a row in a park. There are trees between them which cannot be moved. 
 
 Your task is to rearrange the people by their heights in a non-descending order without moving the trees.

# Example

 For `a = [-1, 150, 190, 170, -1, -1, 160, 180]`, the output should be

 `[-1, 150, 160, 170, -1, -1, 180, 190]`.

# Input/Output


 - `[input]` integer array `a`

    If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.

    Constraints:

    `5 ≤ a.length ≤ 30,`

    `-1 ≤ a[i] ≤ 200.`


 - `[output]` an integer array

    `Sorted` array a with all the trees untouched.
"""

def sort_by_height(a):
    # Extract the heights of people and sort them
    sorted_heights = sorted(x for x in a if x != -1)
    
    # Use an iterator to replace the heights in the original list
    height_iter = iter(sorted_heights)
    
    # Create the result list by replacing non-tree elements with sorted heights
    result = [next(height_iter) if x != -1 else x for x in a]
    
    return result