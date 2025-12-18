"""
QUESTION:
Compare the bias of Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP) estimate under different conditions. 

Implement a function `compare_mle_map_bias` that takes the sample size and prior knowledge accuracy as inputs and returns a string describing whether the MAP estimate's bias is superior, inferior, or equivalent to the MLE.
"""

def compare_mle_map_bias(sample_size, prior_accuracy):
    """
    Compare the bias of Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP) estimate.

    Parameters:
    sample_size (int): The size of the sample.
    prior_accuracy (float): The accuracy of the prior knowledge, ranging from 0 to 1.

    Returns:
    str: A string describing whether the MAP estimate's bias is superior, inferior, or equivalent to the MLE.
    """

    # If the sample size is large, MLE often outperforms MAP, especially when the prior knowledge isn't strong or accurate
    if sample_size > 1000:
        return "MLE bias is superior to MAP"

    # If the prior accuracy is high, MAP can potentially outperform MLE
    if prior_accuracy > 0.8:
        return "MAP bias is superior to MLE"

    # If the prior accuracy is low, MAP could perform worse than MLE
    if prior_accuracy < 0.2:
        return "MAP bias is inferior to MLE"

    # For small sample sizes and medium prior accuracy, MAP and MLE are equivalent
    return "MAP and MLE are equivalent"