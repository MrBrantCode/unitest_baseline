"""
QUESTION:
Implement a function called `string_lengths` that takes a list of strings as input and returns a list of their lengths. The function should be implemented using recursion. If the input list contains nested lists of strings, the function should flatten the nested structure and calculate the lengths of all the strings present in the input list. The function should also implement memoization to avoid redundant calculations. It should handle empty strings, strings containing only whitespace characters, and non-string elements in the input list. The input list can contain a minimum of 10 and a maximum of 20 elements.
"""

def string_lengths(lst):
    cache = {}
    result = []

    def recursive_length(string):
        if string in cache:
            return cache[string]
        length = len(string)
        cache[string] = length
        return length

    def recursive_flatten(lst):
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(recursive_flatten(item))
            elif isinstance(item, str):
                flat_list.append(item)
        return flat_list

    flat_lst = recursive_flatten(lst)

    for string in flat_lst:
        result.append(recursive_length(string))

    return result