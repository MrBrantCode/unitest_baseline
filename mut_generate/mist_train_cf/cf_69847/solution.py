"""
QUESTION:
Write a function `calculate_probability` that takes as input two lists of words: `preceding_sequence` and `generated_sequence`. The function should return the probability of the `generated_sequence` given the `preceding_sequence` using the formula for sequence generation in a Seq2Seq model.
"""

def calculate_probability(preceding_sequence, generated_sequence, probability_model):
    """
    Calculate the probability of the generated_sequence given the preceding_sequence.

    Args:
        preceding_sequence (list): The preceding sequence of words.
        generated_sequence (list): The generated sequence of words.
        probability_model (dict): A dictionary containing the probabilities of each word given the preceding sequence.

    Returns:
        float: The probability of the generated_sequence given the preceding_sequence.
    """
    probability = 1.0
    for i, word in enumerate(generated_sequence):
        # Calculate the probability of the current word given the preceding sequence and generated sequence up to this point
        preceding_context = tuple(preceding_sequence + generated_sequence[:i])
        probability *= probability_model.get((preceding_context, word), 0)
    return probability