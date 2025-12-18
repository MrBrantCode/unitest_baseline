"""
QUESTION:
Write a function called `transform_array_to_string` that takes a multi-dimensional array as input and returns a string of comma-separated values. The array is irregular, containing elements that may be arrays themselves, and the function should handle varying degrees of nesting. The output string should not contain any square brackets, and nested arrays should be flattened before being transformed into a string.
"""

def transform_array_to_string(my_list):
    def flatten(input_list):
        output_list = []
        for i in input_list:
            if isinstance(i, list):
                output_list.extend(flatten(i))
            else:
                output_list.append(i)
        return output_list

    flattened_list = flatten(my_list)
    return ','.join(str(num) for num in flattened_list)