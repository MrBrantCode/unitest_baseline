"""
QUESTION:
Create a function called `find_pairs` that takes in two parameters: a list of integers and a target sum. The function should return a list of all pairs of integers from the input list that add up to the target sum. If there are no such pairs, the function should return an empty list. The function must have a time complexity of O(n^2), where n is the length of the input list.
"""

def find_pairs(lst, target_sum):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target_sum:
                pairs.append([lst[i], lst[j]])
    return pairs