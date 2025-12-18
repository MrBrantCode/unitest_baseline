"""
QUESTION:
Compare the performance of two classification models with different majority classes (70% and 60%) using the provided accuracy scores (0.75 and 0.67). Design a function `compare_model_performance` that takes the accuracy and majority class rate of each model as input and returns a message indicating whether the models can be directly compared based on accuracy alone.
"""

def compare_model_performance(model1_accuracy, model1_majority_class, model2_accuracy, model2_majority_class):
    """
    Compare the performance of two classification models based on their accuracy and majority class rates.

    Args:
    model1_accuracy (float): Accuracy of the first model.
    model1_majority_class (float): Majority class rate of the first model.
    model2_accuracy (float): Accuracy of the second model.
    model2_majority_class (float): Majority class rate of the second model.

    Returns:
    str: A message indicating whether the models can be directly compared based on accuracy alone.
    """
    if model1_majority_class != model2_majority_class:
        return "Models cannot be directly compared due to different majority class rates."
    else:
        return "Models can be directly compared."