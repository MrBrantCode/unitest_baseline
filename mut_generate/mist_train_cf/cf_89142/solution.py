"""
QUESTION:
Write a function `convert_strings_to_floats` that takes an array of strings as input and returns an array of floats. The function should ignore any strings that cannot be directly converted to floats, and round up non-whole number floats to the nearest whole number. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.
"""

def convert_strings_to_floats(strings):
    floats = []
    for string in strings:
        try:
            float_value = float(string)
            if float_value.is_integer():
                floats.append(int(float_value))
            else:
                floats.append(int(float_value) + 1)
        except ValueError:
            pass
    return floats