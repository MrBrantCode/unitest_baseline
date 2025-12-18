"""
QUESTION:
Write a function `calculate_precision` that calculates the precision of a multi-label model by averaging the precision of each sample. The function should take two parameters: `ground_truth` and `prediction`, where both are lists of binary vectors representing the ground truth and predicted labels, respectively. The function should return the precision of the model. Consider whether to include samples with no predictions when calculating the average precision, and document your reasoning in the function's comments.
"""

def calculate_precision(ground_truth, prediction):
    """
    Calculate the precision of a multi-label model by averaging the precision of each sample.

    Args:
        ground_truth (list): A list of binary vectors representing the ground truth labels.
        prediction (list): A list of binary vectors representing the predicted labels.

    Returns:
        float: The precision of the model.
    """

    # Initialize sum of precisions and count of samples with predictions
    total_precision = 0
    samples_with_predictions = 0

    # Iterate over the ground truth and predicted labels
    for gt, pred in zip(ground_truth, prediction):
        # Check if there are any predictions
        if any(pred):
            # Calculate the precision for this sample
            sample_precision = sum([gt[i] and pred[i] for i in range(len(gt))]) / sum(pred)
            # Add the precision to the total and increment the count of samples with predictions
            total_precision += sample_precision
            samples_with_predictions += 1
        else:
            # If there are no predictions, consider the precision as 0 for this sample
            total_precision += 0
            samples_with_predictions += 1

    # Calculate the average precision
    if samples_with_predictions == 0:
        # If there are no samples with predictions, return 0
        return 0
    else:
        # Return the average precision
        return total_precision / samples_with_predictions