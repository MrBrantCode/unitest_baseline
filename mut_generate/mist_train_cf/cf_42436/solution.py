"""
QUESTION:
Implement a method `do_rollouts` that generates sequences of observations and actions based on a given skill and maximum sequence length. The method should iterate over a specified number of sequences and call another method, `do_rollout`, to generate each sequence. The `do_rollout` method takes the skill and maximum path length as parameters and returns a `path` object containing observations. Ensure that the assertion for the shape of the observations in the generated path is properly formatted and verifies the correct length.
"""

def do_rollouts(skill, max_sequence_length, num_sequences):
    """
    Generates sequences of observations and actions based on a given skill and maximum sequence length.

    Args:
        skill (object): The skill to use for rollouts.
        max_sequence_length (int): The maximum length of each sequence.
        num_sequences (int): The number of sequences to generate.

    Returns:
        list: A list of paths, each containing observations and actions.
    """
    paths = []
    for _ in range(num_sequences):
        path = do_rollout(skill, max_sequence_length)
        paths.append(path)
    return paths


def do_rollout(skill, max_path_length):
    """
    Generates a sequence of observations and actions based on a given skill and maximum path length.

    Args:
        skill (object): The skill to use for the rollout.
        max_path_length (int): The maximum length of the path.

    Returns:
        object: A path object containing observations and actions.
    """
    # implementation of do_rollout method
    pass