"""
QUESTION:
Implement a function `get_unique_shortest_substrings(str1, str2)` that takes two input strings `str1` and `str2` of lengths `n` and `m`, respectively, and returns all unique shortest substrings common to both strings. The function should optimize for time efficiency.
"""

def get_unique_shortest_substrings(str1, str2):

    def get_all_substrings(input_string):
        length = len(input_string)
        return set(input_string[i:j+1] for i in range(length) for j in range(i,length))

    substrings1 = get_all_substrings(str1)
    substrings2 = get_all_substrings(str2)

    common_substrings = substrings1 & substrings2

    # find shortest length
    if common_substrings:
        shortest_length = min(len(x) for x in common_substrings)
        shortest_substrings = [x for x in common_substrings if len(x) == shortest_length]
    else:
        shortest_substrings = []

    return shortest_substrings