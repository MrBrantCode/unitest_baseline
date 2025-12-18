"""
QUESTION:
Create a function named `create_dictionary` that takes a list of tuples as input. The function should return a dictionary where each key-value pair is created from the tuples in the list. If a tuple has two elements, the key is the first element and the value is the second element, with the following conversions: if the key is a string, the value is converted to uppercase; if the key is an integer, the value is converted to binary; if the key is a float, the value is rounded to the nearest whole number. If a tuple has three elements, the third element specifies the data type of the value, and the value is converted to that type. The function should have a time complexity of O(n) and a space complexity of O(1), and should not use any built-in functions or libraries for conversions.
"""

def create_dictionary(lst):
    dictionary = {}
    for tup in lst:
        key, value = tup[0], tup[1]
        if len(tup) == 3:
            data_type = tup[2]
            if data_type == "string":
                value = str(value).upper()
            elif data_type == "integer":
                value = bin(int(value))[2:]
            elif data_type == "float":
                value = round(float(value))
        else:
            if isinstance(key, str):
                value = str(value).upper()
            elif isinstance(key, int):
                value = bin(int(value))[2:]
            elif isinstance(key, float):
                value = round(float(value))
        dictionary[key] = value
    return dictionary