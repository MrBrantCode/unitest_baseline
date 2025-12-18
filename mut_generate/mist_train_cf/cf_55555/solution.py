"""
QUESTION:
Write a function `choose_model` that takes in the following information: 
- training data R2 scores for two models, one with 'linear' kernel and the other with 'rbf' kernel 
- test data R2 scores for both models
- training data mean squared error (MSE) for both models
- test data MSE for both models
The function should return a string indicating whether the 'linear' model or 'rbf' model is preferred based on the provided data and considering factors such as interpretability, complexity, and run-time. There are no specific restrictions on the function's output.
"""

def choose_model(train_linear_r2, train_rbf_r2, test_linear_r2, test_rbf_r2, train_linear_mse, train_rbf_mse, test_linear_mse, test_rbf_mse):
    """
    This function compares the performance of 'linear' and 'rbf' kernel models based on their R2 scores and mean squared errors on training and test data.

    Args:
    train_linear_r2 (float): Training data R2 score for the 'linear' model.
    train_rbf_r2 (float): Training data R2 score for the 'rbf' model.
    test_linear_r2 (float): Test data R2 score for the 'linear' model.
    test_rbf_r2 (float): Test data R2 score for the 'rbf' model.
    train_linear_mse (float): Training data mean squared error for the 'linear' model.
    train_rbf_mse (float): Training data mean squared error for the 'rbf' model.
    test_linear_mse (float): Test data mean squared error for the 'linear' model.
    test_rbf_mse (float): Test data mean squared error for the 'rbf' model.

    Returns:
    str: A string indicating whether the 'linear' or 'rbf' model is preferred based on the provided data.
    """

    # Check if the 'rbf' model is overfitting
    if train_rbf_r2 - test_rbf_r2 > 0.1:  # assuming a 0.1 difference as a threshold for overfitting
        return "The 'linear' model is preferred due to potential overfitting in the 'rbf' model."

    # Compare test performance of both models
    if test_rbf_r2 > test_linear_r2:
        return "The 'rbf' model is preferred due to its better test performance."
    elif test_rbf_r2 < test_linear_r2:
        return "The 'linear' model is preferred due to its better test performance."
    else:
        # If test performance is similar, consider other factors such as interpretability, complexity, or run-time
        return "Both models have similar test performance. Consider other factors such as interpretability, complexity, or run-time to make a decision."