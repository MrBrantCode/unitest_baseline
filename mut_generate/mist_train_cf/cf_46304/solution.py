"""
QUESTION:
Split a Chronologically Arranged Dataset into Training and Testing Sets

Write a function `solve` that takes a chronologically arranged dataset as input and splits it into a training set and a testing set. The training set should contain the earliest 20% of the records, and the testing set should contain the remaining 80% of the records. The function should return the training and testing sets. 

The input dataset is a pandas DataFrame sorted in ascending order by date. The function should not shuffle the data or alter the chronological order of the dates.
"""

def solve(features_dataframe):
    """
    Splits a chronologically arranged dataset into training and testing sets.
    
    Args:
    features_dataframe (pandas DataFrame): A pandas DataFrame sorted in ascending order by date.
    
    Returns:
    tuple: A tuple containing the training and testing sets.
    """
    train_size = int(0.2 * len(features_dataframe))
    train_dataframe = features_dataframe[:train_size]
    test_dataframe = features_dataframe[train_size:]
    return train_dataframe, test_dataframe