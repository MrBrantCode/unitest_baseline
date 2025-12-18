"""
QUESTION:
Design a function `greedy_sum_subset` that takes a list of integers `arr` and a target sum `target_sum` as input, and returns the minimum number of subsets of `arr` such that the sum of elements in each subset does not exceed `target_sum`. The function should return a list of subsets, where each subset is a list of integers. The goal is to minimize the number of subsets while ensuring that the sum of elements in each subset does not exceed the target sum.
"""

def greedy_sum_subset(arr, target_sum):
    n = len(arr)

    # Sort the array in decreasing order
    arr.sort(reverse=True)

    # Initialize the list of subsets
    subsets = []

    for i in range(n):
        j = 0
        found = False
        
        # Check if the element can be added to the existing subsets
        while j < len(subsets):
            
            if sum(subsets[j]) + arr[i] <= target_sum:
                subsets[j].append(arr[i])
                found = True
                break
            
            j += 1

        if not found:
            # Create a new subset if no subset can contain the element
            subsets.append([arr[i]])

    return subsets