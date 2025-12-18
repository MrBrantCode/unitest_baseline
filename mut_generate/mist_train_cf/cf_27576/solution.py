"""
QUESTION:
Create a `DataProcessor` class with the following specifications:

The class should have a constructor `__init__` that takes a `source` parameter, representing the source of the data, which should be a string. The class should have three methods: `read_data`, `process_data`, and `output_data`.

The `read_data` method should simulate reading data from the specified source and store it within the class instance. The `process_data` method should apply a specific logic to the read data. The `output_data` method should return the processed data in a specific format.

Note: There are no specific requirements for the data source, data format, and data processing logic, so you can use any suitable implementation.
"""

def entance(source):
    data = [1, 3, 2, 4, 5]  # Example simulated data
    data.sort()
    return data