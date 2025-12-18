"""
QUESTION:
Develop a function named `find_pairs` that takes a list of integers and a target integer as input, and returns a list of tuples where each tuple contains a pair of integers from the list that sum up to the target integer. The function should handle duplicate elements in the list and output the pairs in ascending order based on the first element of each pair. The function should also be efficient for large input lists.
"""

def find_pairs(lst, target_sum):
    pairs = []
    num_count = {}

    for num in lst:
        if target_sum - num in num_count:
            for _ in range(num_count[target_sum - num]):
                pairs.append((target_sum - num, num))

        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

    return sorted(pairs, key=lambda x: x[0])