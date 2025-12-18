"""
QUESTION:
Create a function `find_repeating_pairs` that takes a multidimensional array as input and returns a dictionary containing the count of each pair of identical elements found in the array, including sub-arrays at any level. The function should recursively traverse the array, count the occurrence of each element, and return the count of pairs (i.e., the count of each element divided by 2, rounded down) for elements that appear more than once.
"""

def find_repeating_pairs(arr):
    pair_dict = {}
    def traverse(element):
        if isinstance(element, list):
            for item in element:
                traverse(item)
        else:
            if element in pair_dict:
                pair_dict[element] += 1
            else:
                pair_dict[element] = 1

    traverse(arr)

    repeating_pairs = {k: v//2 for k, v in pair_dict.items() if v > 1}

    return repeating_pairs