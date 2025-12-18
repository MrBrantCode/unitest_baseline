"""
QUESTION:
Write a function `divide_data` that takes a dataframe `df` sorted by timestamp and a percentage `train_size` as input. Divide the dataframe into a training set and a validation set such that the validation set contains more recent timestamps than the training set. The training set should contain `train_size` proportion of the total data.

The input dataframe `df` is already sorted by timestamp. The function should return two dataframes: `train_dataframe` and `validation_dataframe`.
"""

def divide_data(df, train_size):
    """
    Divide a sorted dataframe into training and validation sets.

    Args:
    df (DataFrame): A dataframe sorted by timestamp.
    train_size (float): The proportion of data to include in the training set.

    Returns:
    train_dataframe (DataFrame): The training set.
    validation_dataframe (DataFrame): The validation set.
    """
    split_index = int(len(df) * train_size)
    train_dataframe = df.iloc[:split_index]
    validation_dataframe = df.iloc[split_index:]
    return train_dataframe, validation_dataframe