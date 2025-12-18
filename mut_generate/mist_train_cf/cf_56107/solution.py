"""
QUESTION:
Create a function called `performOperation` that takes a variable number of inputs, where the first argument `num_of_inputs` represents the number of integer inputs that follow. This function should handle the following cases:

- `num_of_inputs` can range from 1 to 3.
- For each input parameter, it should handle the following scenarios:
  - The parameter is a positive integer.
  - The parameter is a negative integer.
  - The parameter is zero.
  - The parameter is a non-integer.
- The function should return the corresponding result(s) for each input parameter.
- The function should include proper error handling for non-integer inputs.

Restrictions: Use Python's dictionary mapping to emulate switch-case conditions.
"""

def performOperation(num_of_inputs, *inputs):
    """
    This function takes a variable number of inputs and handles different scenarios 
    based on the number and value of the inputs.

    Parameters:
    num_of_inputs (int): The number of integer inputs that follow.
    *inputs: A variable number of integer inputs.

    Returns:
    result(s): The corresponding result(s) for each input parameter.
    """
    
    def handleParameter(param):
        """
        This function handles a single input parameter and returns the corresponding result.
        
        Parameters:
        param: An input parameter.

        Returns:
        result: The corresponding result for the input parameter.
        """
        try:
            num = int(param)
            if num == 0:
                return "Zero number"
            elif num > 0:
                return "Positive Number"
            else:
                return "Negative Number"
        except ValueError:
            return "Non-integer input"

    switch = {
        1: lambda inputs: handleParameter(inputs[0]),
        2: lambda inputs: [handleParameter(param) for param in inputs],
        3: lambda inputs: [handleParameter(param) for param in inputs]
    }

    func = switch.get(num_of_inputs, lambda inputs: "Invalid number of inputs")
    return func(inputs)