"""
QUESTION:
Write a function `map_tuples(tpl_list, alpha_str)` that accepts a list of integer tuples `tpl_list` and a string of multiple alphabets `alpha_str` as inputs. The function should replace the second element of each tuple with a numerical value obtained by mapping each alphabet to its position in the string in reverse order. If a tuple's second element can't be mapped with the string, consider it as 0. The function should return a list of tuples sorted by the newly assigned second element in descending order.
"""

def map_tuples(tpl_list, alpha_str):
    # Map each alphabet to its position in the string in reverse order.
    str_map = {ch: len(alpha_str) - i for i, ch in enumerate(alpha_str)}
    # Replace second element of each tuple and sort them.
    result = sorted([(x[0], str_map.get(chr(x[1] + 96), 0)) for x in tpl_list], key=lambda y: -y[1])
    return result