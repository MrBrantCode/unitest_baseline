"""
QUESTION:
Create a function `generate_subsets` that takes a set `input_set` as input and returns all subsets of the set, each containing at least one element from the original set. The function should generate subsets in lexicographically increasing order. The function should handle sets of any size efficiently in terms of time and space complexity.
"""

def generate_subsets(input_set):
    input_set = sorted(input_set)  # Sort the input set lexicographically
    
    n = len(input_set)
    subsets = []
    
    # Generate subsets of different sizes
    for size in range(1, n+1):
        generate_subsets_util(input_set, size, 0, [], subsets)
    
    return subsets


def generate_subsets_util(input_set, size, index, current_subset, subsets):
    # If the current subset has reached the desired size, add it to the subsets list
    if len(current_subset) == size:
        subsets.append(current_subset.copy())
        return
    
    # Generate subsets by including the current element at the index
    for i in range(index, len(input_set)):
        current_subset.append(input_set[i])
        
        # Recursively generate subsets using the remaining elements
        generate_subsets_util(input_set, size, i+1, current_subset, subsets)
        
        current_subset.pop()  # Backtrack and remove the last element