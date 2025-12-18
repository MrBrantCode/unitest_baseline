"""
QUESTION:
Write a function `process_mapping` that takes in a dictionary of tuples as input where each key is an integer and each value is another tuple containing a sequence of integers, a boolean value, and two integers. The function should return a dictionary where the keys are the original integer keys and the values are calculated based on the following rules: 

- If the boolean value is True, the result is the sum of the sequence of integers multiplied by the first integer.
- If the boolean value is False, the result is the second integer multiplied by the first integer.
"""

def process_mapping(tuples):
    result_dict = {}
    for key, value in tuples.items():
        sequence, is_valid, count, multiplier = value
        if is_valid:
            result = sum(sequence) * multiplier
        else:
            result = count * multiplier
        result_dict[key] = result
    return result_dict