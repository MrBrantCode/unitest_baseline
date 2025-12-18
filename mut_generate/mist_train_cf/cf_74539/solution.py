"""
QUESTION:
Write a function named `count_different_elements` that takes two tuples, `t1` and `t2`, as input. The function should compare the elements of `t1` and `t2`, including any nested tuples, and return a dictionary where the keys are the elements that are not common to both tuples, and the values are tuples containing the count of the element and a string indicating the originating tuple ("tuple1" or "tuple2"). If an element is found in both tuples, the value should be a list of counts from both tuples and the string "both". The function should handle nested tuples by flattening them before comparison.
"""

def count_different_elements(t1, t2):
    def flatten_tuple(t):
        result = []
        for i in t:
            if isinstance(i, tuple):
                result.extend(flatten_tuple(i))
            else:
                result.append(i)
        return tuple(result)

    t1 = flatten_tuple(t1)
    t2 = flatten_tuple(t2)

    t1_counter = dict()
    t2_counter = dict()
    for element in t1:
        t1_counter[element] = t1_counter.get(element, 0) + 1
    for element in t2:
        t2_counter[element] = t2_counter.get(element, 0) + 1

    t1_diff_elements = set(t1_counter.keys()) - set(t2_counter.keys())
    t2_diff_elements = set(t2_counter.keys()) - set(t1_counter.keys())
    common_elements = set(t1_counter.keys()) & set(t2_counter.keys())

    result = {}
    for element in t1_diff_elements:
        result[element] = (t1_counter[element], 'tuple1')
    for element in t2_diff_elements:
        result[element] = (t2_counter[element], 'tuple2')
    for element in common_elements:
        result[element] = ([t1_counter[element], t2_counter[element]], 'both')

    return result