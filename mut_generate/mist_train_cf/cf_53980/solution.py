"""
QUESTION:
Write a function named `split_dataset` to divide a dataset into a training set and a testing set. The function should take a pandas DataFrame `features_dataframe` as input, with a column of chronologically arranged dates. The function should return two DataFrames, `train_dataframe` and `test_dataframe`, where `train_dataframe` contains 80% of the data with the most recent dates and `test_dataframe` contains the remaining 20% of the data with the earliest dates.
"""

def split_dataset(features_dataframe):
    """
    Divide a dataset into a training set and a testing set.
    
    Parameters:
    features_dataframe (pandas DataFrame): A DataFrame with a column of chronologically arranged dates.
    
    Returns:
    train_dataframe (pandas DataFrame): A DataFrame containing 80% of the data with the most recent dates.
    test_dataframe (pandas DataFrame): A DataFrame containing the remaining 20% of the data with the earliest dates.
    """
    # assuming "date" is the column that holds the dates and is of type pd.datetime
    features_dataframe = features_dataframe.sort_values("date")
    split_point = int(len(features_dataframe) * 0.8)
    train_dataframe = features_dataframe.iloc[:split_point]
    test_dataframe = features_dataframe.iloc[split_point:]
    return train_dataframe, test_dataframe