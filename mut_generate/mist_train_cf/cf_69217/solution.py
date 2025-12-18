"""
QUESTION:
Create a function called `manipulate_variables` that accepts a pandas DataFrame as input, filters rows based on the 'Age' column, sorts the resulting DataFrame by 'Age' in descending order, and adds a new column 'IsAdult' based on the 'Age' column. The function should return the manipulated DataFrame and handle cases where the input is not a pandas DataFrame.
"""

import pandas as pd

def entance(dataset):
    # Check if input is of correct type
    if not isinstance(dataset, pd.DataFrame):
        return "Error: Input should be a pandas DataFrame"
        
    # Perform data manipulation
    # For example: Filter rows where 'Age' is greater than 30
    filtered_dataset = dataset[dataset['Age'] > 30]
    
    # Sort by 'Age' in descending order
    sorted_dataset = filtered_dataset.sort_values(by='Age', ascending=False)
    
    # Add a new column 'IsAdult' which is True if 'Age' is above 18, False otherwise
    sorted_dataset['IsAdult'] = sorted_dataset['Age'].apply(lambda x: True if x > 18 else False)
    
    return sorted_dataset