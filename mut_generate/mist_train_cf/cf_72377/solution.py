"""
QUESTION:
Write a function `find_most_common` that takes a list of mixed data types as input, including integers, floats, strings, dictionaries, and lists (nested to any depth), and returns the most common value(s) in the input data. The function should recursively traverse the nested data structures, count the occurrences of each value, and return the value(s) with the highest frequency. If multiple values have the same highest frequency, the function should return all of them.
"""

def find_most_common(data):
    def find_most_common_recursive(data, counts):
        if isinstance(data, dict):
            for v in data.values():
                find_most_common_recursive(v, counts)
        elif isinstance(data, list):
            for item in data:
                find_most_common_recursive(item, counts)
        elif isinstance(data, (int, float, str)):
            counts[data] = counts.get(data, 0) + 1

    counts = {}
    find_most_common_recursive(data, counts)

    max_count = max(counts.values())
    most_common = [k for k, v in counts.items() if v == max_count]

    if len(most_common) > 1:
        return most_common
    else:
        return most_common[0]