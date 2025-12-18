"""
QUESTION:
Write a function `calculate_nlp_efficiency` that takes in a list of tuples representing the model's performance metrics, where each tuple contains the accuracy, precision, and recall of the model on a specific dataset. The function should return the average accuracy of the model across all datasets. The model's performance is considered acceptable if the average accuracy is above a certain threshold (0.8).
"""

def calculate_nlp_efficiency(metrics):
    """
    Calculate the average accuracy of the model across all datasets.

    Args:
    metrics (list): A list of tuples containing the accuracy, precision, and recall of the model on each dataset.

    Returns:
    float: The average accuracy of the model across all datasets.
    """
    # Initialize sum of accuracy
    total_accuracy = 0
    
    # Iterate over each metric in the list
    for metric in metrics:
        # Extract the accuracy from the tuple
        accuracy = metric[0]
        
        # Add the accuracy to the total
        total_accuracy += accuracy
    
    # Calculate the average accuracy
    average_accuracy = total_accuracy / len(metrics)
    
    return average_accuracy