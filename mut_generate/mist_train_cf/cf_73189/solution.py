"""
QUESTION:
Develop a Python function named `nested_index` that takes a nested list `arr` and a number `num` as input. The function should return a string in the format "frequency: x, indices: y" where x is the frequency of `num` in the flattened list and y is a list of the first two indices of `num` in the flattened list. The function should be able to handle nested lists of arbitrary depth.
"""

def nested_index(arr, num):
    def flatten(lst):
        for i, el in enumerate(lst):
            try: yield from flatten(el)
            except TypeError: yield el
  
    flat_list = list(flatten(arr))
    freq = flat_list.count(num)
    indices = [i for i, x in enumerate(flat_list) if x == num][:2]
    return "frequency: {}, indices: {}".format(freq, indices)