"""
QUESTION:
Create a function named `generate_subsets` that takes a set of elements as input and returns all subsets containing at least one element from the original set. The subsets should be generated in lexicographically increasing order, and the function should efficiently handle input sets of any size, with a time complexity of O(2^n) and a space complexity of O(2^n), where n is the size of the input set.
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