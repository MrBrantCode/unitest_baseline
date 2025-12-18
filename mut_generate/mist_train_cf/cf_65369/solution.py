"""
QUESTION:
Create a function `check_order_min_dist` that takes three parameters: two number strings (`string1` and `string2`) and an integer `min_dist` representing the minimum number of digits between matching digits in `string1`. The function should return `True` if all digits of `string2` appear in the same order in `string1` and the distance between consecutive occurrences of the same digit in `string1` is at least `min_dist`. Return `False` otherwise.
"""

def check_order_min_dist(string1, string2, min_dist):
    for item in string2:
        if item in string1:
            indices = [i for i, x in enumerate(string1) if x == item]
            if len(indices) > 1:
                min_distance = min([indices[i] - indices[i - 1] for i in range(1, len(indices))])
                if min_distance < min_dist:
                    return False
        else:
            return False
    order_string1 = [x for x in string1 if x in string2]
    return ''.join(order_string1) == string2