"""
QUESTION:
Calculate the geometric mean from a multi-level list of integers with unpredictable depth. Create a custom exception to handle situations where a zero or negative number is found in the list, as these values are incompatible with the geometric mean computation. This exception should yield a detailed error message and request the user to provide a fresh list. 

The function should be named `calculate_geometric_mean` and it should take one argument, `multi_level_list`, which is the input list. The function should return the geometric mean if all numbers in the list are positive, otherwise it should raise the custom exception.
"""

class InvalidValueException(Exception):
    pass

def calculate_geometric_mean(multi_level_list):
    from functools import reduce
    from math import pow
    def flatten(lis):
        for item in lis:
            if isinstance(item, list):
                for x in flatten(item):
                    yield x
            else:
                yield item
    try:
        flat_list = list(flatten(multi_level_list))
        if any(i <= 0 for i in flat_list):
            raise InvalidValueException
        return pow(reduce((lambda x, y: x * y), flat_list), 1/len(flat_list))
    except InvalidValueException:
        print('Error: The list contains a zero or negative number. '
              'These values are incompatible with the geometric mean computation. '
              'Please provide a fresh list.')