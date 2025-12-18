"""
QUESTION:
Implement a function named `handle_skewed_labels` that handles the issue of skewed labels in a deep neural network model where the labels are capped at a certain value (e.g. 90th percentile) and the model performs well in general but degrades for users with high value labels. The function should be able to handle the following restrictions:

- The model should perform well for both users with low and high value labels.
- The function should not degrade business metrics for users with low number of activities.
- The solution can involve data transformation, sampling methods, ensemble models, multi-task learning, weighted loss functions, or adding new features.
"""

def handle_skewed_labels(labels, threshold=0.9):
    """
    This function handles skewed labels in a deep neural network model.
    
    Parameters:
    labels (list): A list of label values
    threshold (float): The percentile threshold to cap the labels (default is 0.9)
    
    Returns:
    list: A list of transformed labels
    """
    
    # Calculate the threshold value
    threshold_value = np.percentile(labels, threshold * 100)
    
    # Cap the labels at the threshold value
    capped_labels = np.minimum(labels, threshold_value)
    
    # Apply logarithmic transformation to the capped labels
    transformed_labels = np.log(capped_labels + 1)
    
    return transformed_labels