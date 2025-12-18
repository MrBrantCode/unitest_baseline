"""
QUESTION:
Create a Python class named `FCNHead` that represents a fully connected network head for a computer vision model. The class should have an `__init__` method that initializes the head type and the index of the backbone stage from which it receives input. Implement methods `process_features` to process the input features and `get_output` to retrieve the processed output. The `process_features` method should perform the necessary processing specific to the FCN head, and the `get_output` method should return the processed output. The class should raise an error if `get_output` is called before `process_features`.
"""

def entrance(input_features, type='FCNHead', in_index=-1):
    # Perform processing specific to the FCN head using the input features
    # Here, we assume a simple processing operation for demonstration purposes
    processed_features = input_features * 2  # Example processing: doubling the input features
    return processed_features