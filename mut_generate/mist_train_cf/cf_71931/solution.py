"""
QUESTION:
Implement a function `avoid_data_augmentation_bias` that determines whether a data augmentation technique may lead to bias in a classification model, considering factors like overfitting and underfitting. The function should take into account the type of data augmentation (over-sampling or under-sampling) and the task type (e.g., image classification).
"""

def avoid_data_augmentation_bias(data_augmentation_type, task_type):
    """
    Determines whether a data augmentation technique may lead to bias in a classification model.
    
    Parameters:
    data_augmentation_type (str): The type of data augmentation (over-sampling or under-sampling)
    task_type (str): The type of task (e.g., image classification)
    
    Returns:
    str: A message indicating whether the data augmentation technique may lead to bias
    """
    
    # Check if data augmentation type is over-sampling
    if data_augmentation_type == "over-sampling":
        # Over-sampling minor class examples could lead to overfitting
        return "Over-sampling may lead to overfitting."
    
    # Check if data augmentation type is under-sampling
    elif data_augmentation_type == "under-sampling":
        # Under-sampling major class instances may lead to underfitting
        return "Under-sampling may lead to underfitting."
    
    # Check if task type is image classification
    elif task_type == "image classification":
        # Data augmentation in the form of rotation, shifting or flipping can cause an unintended bias
        return "Data augmentation may lead to bias in image classification tasks."
    
    # If none of the above conditions are met
    else:
        return "Data augmentation technique may not lead to bias."