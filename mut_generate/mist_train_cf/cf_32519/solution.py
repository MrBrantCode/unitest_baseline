"""
QUESTION:
Create a function called `process_dataframes` that takes three parameters: `load_time` (integer) representing the time taken to load dataframes in seconds, `dataframes` (list) containing the dataframes to be split, and `split_ratio` (float) specifying the ratio for splitting dataframes into training and validation sets. The function should calculate the load time in minutes and seconds, display the information, split the dataframes, and return the training and validation sets as a tuple `(training_set, validation_set)`.
"""

def process_dataframes(load_time, dataframes, split_ratio):
    load_min = load_time // 60  # Calculate minutes
    load_sec = load_time % 60   # Calculate remaining seconds
    print('Dataframes loaded in {} minutes {} seconds! Splitting for train and validation...\n'.format(load_min, load_sec))

    # Split the dataframes into training and validation sets
    split_index = int(len(dataframes) * split_ratio)
    training_set = dataframes[:split_index]
    validation_set = dataframes[split_index:]

    return (training_set, validation_set)