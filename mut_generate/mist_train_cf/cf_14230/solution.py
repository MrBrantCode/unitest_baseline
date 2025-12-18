"""
QUESTION:
Construct a pandas dataframe from a list of dictionaries where each dictionary represents a person with keys 'name', 'age', 'weight', 'height', 'income', 'job', 'city', and 'country'. The dataframe should satisfy the following constraints: 
- 'name' and 'city' should not contain duplicate values, 
- 'age' should be a positive integer, 
- 'weight' should be between 50 and 100, 
- 'height' should be between 150 and 200, 
- 'income' should be greater than 2000, 
- 'job' should be either 'engineer', 'teacher', or 'secretary', 
- 'country' should be either 'Scotland', 'USA', or 'France'. 

Create the function `construct_dataframe` that takes a list of dictionaries as input and returns a pandas dataframe satisfying the above constraints.
"""

import pandas as pd

def construct_dataframe(data):
    """
    Construct a pandas dataframe from a list of dictionaries where each dictionary represents a person.

    Args:
        data (list): A list of dictionaries where each dictionary contains 'name', 'age', 'weight', 'height', 'income', 'job', 'city', and 'country' keys.

    Returns:
        pd.DataFrame: A pandas dataframe satisfying the constraints.
    """
    # Create a pandas DataFrame
    df = pd.DataFrame(data)

    # Apply additional constraints
    df = df.drop_duplicates(subset='name')
    df = df[df['age'] > 0]
    df = df[(df['weight'] >= 50) & (df['weight'] <= 100)]
    df = df[(df['height'] >= 150) & (df['height'] <= 200)]
    df = df[df['income'] > 2000]
    df = df[df['job'].isin(['engineer', 'teacher', 'secretary'])]
    df = df.drop_duplicates(subset='city', keep='first')  # keep the first occurrence of each city
    df = df[df['country'].isin(['Scotland', 'USA', 'France'])]

    return df