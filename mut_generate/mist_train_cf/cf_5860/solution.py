"""
QUESTION:
Write a function `convert_strings_to_floats` that takes an array of strings as input and returns an array of integers. The function should attempt to convert each string to a float, ignore any strings that cannot be converted, and round up non-integer floats to the nearest whole number. The function should have a time complexity of O(n), where n is the number of elements in the array, and a space complexity of O(n).
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