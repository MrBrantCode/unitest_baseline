"""
QUESTION:
Create a Python function named `instantiate_data_type` that accepts a list of mixed data types. The function should instantiate a class for each element in the list based on its data type (String, Float, or Integer), storing the actual value as an attribute for that instance. Each class should have a method to print out the data type and the stored value. The instantiated classes should be returned as a list. The `instantiate_data_type` function should work correctly for lists containing any combination of strings, floats, and integers.
"""

class DataType():
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{str(type(self.value))}: {str(self.value)}"

class String(DataType):
    def __init__(self, value):
        super().__init__(value)

class Float(DataType):
    def __init__(self, value):
        super().__init__(value)

class Integer(DataType):
    def __init__(self, value):
        super().__init__(value)

def instantiate_data_type(data):
    data_types = []
    for d in data:
        if isinstance(d, str):
            data_types.append(String(d))
        elif isinstance(d, float):
            data_types.append(Float(d))
        elif isinstance(d, int):
            data_types.append(Integer(d))
    return data_types