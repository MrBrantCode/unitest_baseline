"""
QUESTION:
Create a function called `compare_tuples(t1, t2)` that takes two tuples as input, where each tuple may contain nested tuples, lists, or sets. The function should return a dictionary where the keys are elements that are not identical in both tuples, and the values are tuples containing the frequency of the element in each tuple and the tuple of origin. If an element is present in both tuples, the frequency should be a list in the format [frequency from tuple1, frequency from tuple2] and the string "both". If an element is unique to one tuple, the frequency should be a single integer and the string "tuple1" or "tuple2". The function should handle any level of nesting and any combination of tuples, lists, and sets within the input tuples.
"""

from collections import Counter
from itertools import chain

def flatten(input):
    output = []
    for i in input:
        if isinstance(i, (tuple, list, set)):
            output.extend(flatten(i))
        else:
            output.append(i)
    return output

def compare_tuples(t1, t2):
    flat_t1 = flatten(t1)
    flat_t2 = flatten(t2)
    
    freq_t1 = Counter(flat_t1)
    freq_t2 = Counter(flat_t2)
    
    keys = set(chain(freq_t1.keys(), freq_t2.keys()))
    
    result = {}
    for key in keys:
        freq_1 = freq_t1.get(key, 0)
        freq_2 = freq_t2.get(key, 0)
        
        if freq_1 > 0 and freq_2 > 0:
            result[key] = ([freq_1, freq_2], 'both')
        elif freq_1 > 0:
            result[key] = (freq_1, 'tuple1')
        else:
            result[key] = (freq_2, 'tuple2')
            
    return result