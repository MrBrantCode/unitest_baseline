"""
QUESTION:
Create a function called `suggest_initial_xgb_hyperparameters` that takes in the number of training examples and the number of features as input. Based on the information provided, return a dictionary with suggested initial values for 'n_estimators', 'learning_rate', and 'max_depth' for an XGBClassifier model, considering the trade-offs between model complexity, overfitting, and training time. The suggested hyperparameters should be reasonable defaults and not necessarily the optimal values, as they may vary depending on the specific dataset and problem at hand.
"""

def suggest_initial_xgb_hyperparameters(num_samples, num_features):
    """
    Suggests initial hyperparameters for XGBClassifier model.

    Args:
    num_samples (int): Number of training examples.
    num_features (int): Number of features.

    Returns:
    dict: Dictionary with suggested initial values for 'n_estimators', 'learning_rate', and 'max_depth'.
    """
    # Reasonable default for number of estimators (trees) in the model
    n_estimators = 100
    
    # Commonly used learning rate (eta) to control the contribution of each tree
    learning_rate = 0.3
    
    # Good starting point for maximum depth per tree
    max_depth = 3
    
    # Return suggested hyperparameters as a dictionary
    return {
        'n_estimators': n_estimators,
        'learning_rate': learning_rate,
        'max_depth': max_depth
    }