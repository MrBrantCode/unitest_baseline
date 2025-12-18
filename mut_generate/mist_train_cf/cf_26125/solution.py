"""
QUESTION:
Write a function `find_pairs_with_sum` that takes three inputs: two lists of integers and a target sum. The function should return all unique pairs of integers, one from each list, whose sum equals the target sum.
"""

def find_pairs_with_sum(list1, list2, target_sum):
    pairs = set()
    for num1 in list1:
        for num2 in list2:
            if num1 + num2 == target_sum:
                pair = tuple(sorted((num1, num2)))
                pairs.add(pair)
    return list(pairs)