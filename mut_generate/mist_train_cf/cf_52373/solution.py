"""
QUESTION:
Write a function called `compare_mle_map` to compare Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP) estimates. The function should describe the conditions under which MLE and MAP are equivalent, superior, or inferior to each other. The function should consider the impact of the amount of data and prior knowledge about the hidden parameters on the comparison.
"""

def compare_mle_map(amount_of_data, prior_knowledge):
    """
    Compare Maximum Likelihood Estimate (MLE) and Maximum A Posteriori (MAP) estimates.

    Parameters:
    amount_of_data (str): The amount of data available. Can be 'limited' or 'enough'.
    prior_knowledge (str): The prior knowledge about the hidden parameters. Can be 'available' or 'unavailable'.

    Returns:
    str: A description of the comparison between MLE and MAP estimates.
    """
    
    if prior_knowledge == 'unavailable':
        if amount_of_data == 'limited':
            return "MLE and MAP are equivalent."
        else:
            return "MLE might be superior to MAP due to its ability to capture the complexity of the data distribution better."
    else:
        if amount_of_data == 'limited':
            return "MAP might be superior to MLE due to its regularization ability."
        else:
            return "MLE and MAP are comparable, with MLE potentially being superior due to its ability to capture the complexity of the data distribution better."