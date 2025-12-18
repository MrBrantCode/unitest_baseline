"""
QUESTION:
Implement a function `process_sequence` that takes a sequence of data as input and returns the output after processing the sequence using a Recurrent Neural Network (RNN) architecture, where the outputs from the previous layer are used as inputs to the next layer, allowing the network to remember the context of the data sequentially.
"""

def process_sequence(sequence):
    """
    Process a sequence of data using a Recurrent Neural Network (RNN) architecture.

    Args:
        sequence (list): A sequence of data.

    Returns:
        list: The output after processing the sequence.
    """
    # Initialize the output list
    output = []

    # Process each item in the sequence
    for i in range(len(sequence)):
        # If it's the first item, use a default previous output
        if i == 0:
            previous_output = 0
        else:
            previous_output = output[i-1]

        # Calculate the current output using the current item and the previous output
        current_output = sequence[i] + previous_output

        # Append the current output to the output list
        output.append(current_output)

    return output