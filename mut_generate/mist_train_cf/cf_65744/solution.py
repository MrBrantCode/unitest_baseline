"""
QUESTION:
Implement the 'decision_tree_ensemble' function, which takes a list of decision tree predictions as input and returns the averaged output. The function should accept a list of lists of numbers representing the predictions from multiple decision trees and return a list of numbers representing the averaged predictions. The length of the input list and the sublists should be the same, representing the number of predictions and the number of decision trees respectively.
"""

def decision_tree_ensemble(predictions):
    """
    This function takes a list of decision tree predictions and returns the averaged output.

    Args:
        predictions (list): A list of lists of numbers representing the predictions from multiple decision trees.

    Returns:
        list: A list of numbers representing the averaged predictions.
    """
    return [sum(prediction) / len(prediction) for prediction in zip(*predictions)]