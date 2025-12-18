"""
QUESTION:
Implement the function `calculate_total_parameters(batch_size, tensor_shapes)` to calculate the total number of parameters in a neural network flow model. The function takes two inputs: 
- `batch_size`: an integer representing the batch size, 
- `tensor_shapes`: a list of tuples representing the shapes of tensors involved in the flow model, where each tuple contains the shape of a tensor with the first dimension representing the batch size.

The function should return the total number of parameters, where the parameters are represented by tensors of shape (batch_size, m_i) for each flow step i.
"""

def calculate_total_parameters(batch_size, tensor_shapes):
    total_params = 0
    for shape in tensor_shapes:
        total_params += shape[1]  # Add the number of parameters in each flow step
    return total_params