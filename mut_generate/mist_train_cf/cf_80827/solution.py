"""
QUESTION:
Create a function called `count_data_types` that takes an array of elements as input and returns a dictionary with the frequency of different data types. The function should count the occurrences of the following data types: positive integers, negative integers, zero, floating point numbers, and strings. The function should ignore other data types.
"""

def count_data_types(arr):
    results = {"positive_int": 0, "negative_int": 0, "zero": 0, "float": 0, "str": 0}
    for elem in arr:
        if isinstance(elem, int):
            if elem > 0:
                results["positive_int"] += 1
            elif elem < 0:
                results["negative_int"] += 1
            else:
                results["zero"] += 1
        elif isinstance(elem, float):
            results["float"] += 1
        elif isinstance(elem, str):
            results["str"] += 1
    return results