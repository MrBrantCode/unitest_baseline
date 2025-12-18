"""
QUESTION:
Implement a function `mask_sequence` that takes a sequence of varying lengths and returns the padded sequence along with a mask to indicate the original parts of the sequence. The function should be able to handle sequences of different lengths and the padded value should be zero.

Restrictions: The function should not modify the input sequences. The padded sequences should be the same length. The mask should be a binary sequence where 1 indicates the original part of the sequence and 0 indicates the padded part.
"""

def mask_sequence(sequences):
    """
    This function takes a list of sequences of varying lengths, pads them to the same length with zeros, 
    and returns the padded sequences along with a mask to indicate the original parts of the sequences.

    Args:
        sequences (list of lists): A list of sequences of varying lengths.

    Returns:
        padded_sequences (list of lists): The padded sequences.
        mask (list of lists): A binary mask where 1 indicates the original part of the sequence and 0 indicates the padded part.
    """

    # Find the maximum length of the sequences
    max_length = max(len(seq) for seq in sequences)

    # Initialize the padded sequences and the mask
    padded_sequences = []
    mask = []

    # Iterate over each sequence
    for seq in sequences:
        # Calculate the padding length
        padding_length = max_length - len(seq)

        # Pad the sequence with zeros
        padded_seq = seq + [0] * padding_length

        # Create a binary mask where 1 indicates the original part of the sequence and 0 indicates the padded part
        seq_mask = [1] * len(seq) + [0] * padding_length

        # Append the padded sequence and the mask to the lists
        padded_sequences.append(padded_seq)
        mask.append(seq_mask)

    return padded_sequences, mask