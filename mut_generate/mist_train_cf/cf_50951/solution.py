"""
QUESTION:
Create a function named `generate_target_sequence` to generate the target sequence for the transformer's decoder in a time-series forecasting problem. The function should take a list of numbers representing the sequence as input and return the input sequence to the decoder and the output/target sequence. The input sequence to the decoder should be shifted right by one time step from the original sequence, with a specified starting token added at the beginning. The starting token can be a fixed number or a vector, depending on the task requirements.
"""

def generate_target_sequence(sequence, bos_token=0):
    """
    Generate the target sequence for the transformer's decoder in a time-series forecasting problem.

    Args:
        sequence (list): A list of numbers representing the sequence.
        bos_token (int, optional): The starting token. Defaults to 0.

    Returns:
        tuple: The input sequence to the decoder and the output/target sequence.
    """
    # Shift the sequence to the right by one time step and add the bos_token at the beginning
    decoder_input = [bos_token] + sequence[:-1]
    # The target sequence is the original sequence
    target_sequence = sequence
    return decoder_input, target_sequence