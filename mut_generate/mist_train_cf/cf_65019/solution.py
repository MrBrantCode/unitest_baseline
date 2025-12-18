"""
QUESTION:
Write a function `compare_mle_map_bias` that compares the bias of Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP) estimate. Consider the scenarios where the bias of MAP estimate is superior, inferior, or equal to the MLE. Explain the conditions under which each scenario might occur, based on the quality and accuracy of prior information.
"""

def compare_mle_map_bias(mle_estimate, map_estimate, prior_information):
    """
    Compare the bias of Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP) estimate.

    Args:
        mle_estimate (float): The Maximum Likelihood Estimate value.
        map_estimate (float): The Maximum A Posteriori Estimate value.
        prior_information (str): The quality of prior information ('reliable', 'misleading', or 'noninformative').

    Returns:
        str: A string describing the scenario where the bias of MAP estimate is superior, inferior, or equal to the MLE.
    """

    if prior_information == 'reliable':
        # MAP estimate is superior to MLE
        return "The MAP estimate is superior to the MLE."
    elif prior_information == 'misleading':
        # MAP estimate is inferior to MLE
        return "The MAP estimate is inferior to the MLE."
    elif prior_information == 'noninformative':
        # MAP estimate is equal to MLE
        return "The MAP estimate is equal to the MLE."
    else:
        # Unknown prior information
        return "Unknown prior information."