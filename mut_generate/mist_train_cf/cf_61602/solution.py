"""
QUESTION:
Write a function `find_max_pairs` that takes a list of pairs of numbers as input and returns a tuple containing the maximum value from any pair and a list of all pairs that contain this maximum value. The function should be able to handle duplicate maximum values in different pairs.
"""

def find_max_pairs(pairs):
    # initialize max_value and max_pairs
    max_value = float('-inf')
    max_pairs = []

    # loop through each pair
    for pair in pairs:
        # loop through each number in the pair
        for num in pair:
            # if current number is greater than max_value
            if num > max_value:
                max_value = num  # update max_value
                max_pairs = [pair]  # update max_pairs
            elif num == max_value:  # if current number is equal to max_value
                max_pairs.append(pair)  # add the pair to max_pairs

    return max_value, max_pairs