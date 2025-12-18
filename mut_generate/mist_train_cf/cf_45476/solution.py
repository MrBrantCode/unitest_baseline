"""
QUESTION:
Write a function named `avoid_data_leakage` that explains why Label Encoding before train-test split is considered data leakage and demonstrate this with an example of a categorical feature having different labels in the train and test set. Assume that the function will handle a pandas DataFrame as input containing a categorical column and return a clear explanation of the issue with the provided example. The function should not include any machine learning model training or evaluation code.
"""

def avoid_data_leakage(df):
    """
    Explains why Label Encoding before train-test split is considered data leakage 
    and demonstrates this with an example of a categorical feature having different 
    labels in the train and test set.

    Args:
        df (pandas DataFrame): Input DataFrame containing a categorical column.

    Returns:
        str: Explanation of the issue with the provided example.
    """

    explanation = "Applying Label Encoding before splitting the data can cause information from the test set to leak into the training set. "
    explanation += "If the categorical feature has different labels in the train and test set, Label Encoding might create a misleading numerical relationship. "
    explanation += "Such leakage can cause an unrealistic optimistic performance evaluation. "
    explanation += "The usual practice is to split the data first into train and test, and then apply any preprocessing steps separately on these sets to avoid such data leakage."

    return explanation