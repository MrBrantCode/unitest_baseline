"""
QUESTION:
Construct a function `count_pairs` that calculates the number of unique pairs in a list of numbers whose combined sum matches a given 'sum'. The function should take two parameters: a list of numbers and the target sum. The pairs should be unique, implying that if the pair (a, b) is considered, then (b, a) should not be counted as a separate pair. The function should not use any pre-existing Python functions or libraries and should handle edge cases such as an empty list or a list with only one element, as well as negative numbers and zero. The function should be efficient in terms of time and space complexity, and should handle large lists of numbers (up to 10^6 elements) efficiently.
"""

def count_pairs(lst, target_sum):
    elements = {} 
    pair_set = set()
    count = 0

    for num in lst:
        remainder = target_sum - num
        # Checking if pair (num, remainder) or (remainder, num) is already counted
        if remainder in elements and (num, remainder) not in pair_set and (remainder, num) not in pair_set:
            count += 1
            pair_set.add((num, remainder))

        else:
            elements[num] = num

    return count