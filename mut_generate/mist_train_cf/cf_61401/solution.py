"""
QUESTION:
Create a function named `analyze_music_study` that takes no arguments. Illustrate concepts in experimental design, including the placebo effect, control group, and sampling error, in the context of a study examining the influence of varied musical genres on worker efficiency.
"""

def analyze_music_study(data):
    """
    Analyze the music study data.

    Args:
        data (dict): A dictionary containing the study data.
            - 'control_group': A list of productivity scores for the control group.
            - 'experimental_groups': A dictionary with music genres as keys and lists of productivity scores as values.

    Returns:
        dict: A dictionary containing the analysis results.
            - 'control_group_mean': The mean productivity score of the control group.
            - 'experimental_group_means': A dictionary with music genres as keys and mean productivity scores as values.
            - 'sampling_error': A rough estimate of the sampling error (standard deviation of the control group).
    """

    # Calculate the mean productivity score of the control group
    control_group_mean = sum(data['control_group']) / len(data['control_group'])

    # Calculate the mean productivity scores of the experimental groups
    experimental_group_means = {}
    for genre, scores in data['experimental_groups'].items():
        experimental_group_means[genre] = sum(scores) / len(scores)

    # Calculate a rough estimate of the sampling error (standard deviation of the control group)
    import numpy as np
    sampling_error = np.std(data['control_group'])

    return {
        'control_group_mean': control_group_mean,
        'experimental_group_means': experimental_group_means,
        'sampling_error': sampling_error
    }