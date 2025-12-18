"""
QUESTION:
Develop a function named `non_identical_frequency` that takes two tuples as input. The function should compare the two tuples, identifying non-identical elements and their frequency in each tuple, including nested tuples and other data structures such as lists, sets, and dictionaries. The function should return a dictionary where the keys are the non-identical elements and the values are tuples containing the frequency and the originating tuple ("tuple1", "tuple2", or "both"). If a non-identical element is a function, the function name should be used as the key; if the function is anonymous, the key should be 'anonymous_function'.
"""

from collections import Counter
from itertools import chain
import types

def non_identical_frequency(t1, t2):
    def flatten_tuple(t):
        flat_list = []
        for elem in t:
            if isinstance(elem, (tuple, list, set)):
                flat_list.extend(flatten_tuple(elem))
            elif isinstance(elem, dict):
                flat_list.extend(flatten_tuple(list(elem.items())))
            elif isinstance(elem, types.FunctionType):
                flat_list.append('anonymous_function' if elem.__name__ == '<lambda>' else elem.__name__)
            else:
                flat_list.append(elem)
        return flat_list

    flat_t1 = flatten_tuple(t1)
    flat_t2 = flatten_tuple(t2)
    
    counter_t1 = Counter(flat_t1)
    counter_t2 = Counter(flat_t2)

    non_identical_dict = {}
    for k in set(chain(counter_t1.keys(), counter_t2.keys())):
        if k in counter_t1 and k in counter_t2:
            if counter_t1[k] != counter_t2[k]:
                non_identical_dict[k] = ([counter_t1[k], counter_t2[k]], "both")
        elif k in counter_t1:
            non_identical_dict[k] = ([counter_t1[k], 0], "tuple1")
        else:
            non_identical_dict[k] = ([0, counter_t2[k]], "tuple2")
    
    return non_identical_dict