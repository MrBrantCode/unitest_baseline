"""
QUESTION:
In the context of a Transformer model, describe how the keys (K) and values (V) are derived from the encoder's output to be used in the decoder's second attention layer, and explain why K and V have the same vector representations despite being used for different languages.
"""

def derive_keys_values(encoder_output, weight_matrices):
    """
    Derive keys (K) and values (V) from the encoder's output.

    Parameters:
    - encoder_output: Output from the encoder
    - weight_matrices: Weight matrices for key and value derivation

    Returns:
    - K (key) and V (value) derived from the encoder's output
    """
    keys = encoder_output @ weight_matrices["key"]
    values = encoder_output @ weight_matrices["value"]
    return keys, values