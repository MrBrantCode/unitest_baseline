"""
QUESTION:
Construct a pandas dataframe from four dictionaries with the following constraints:
- The dataframe should not contain duplicate values in the 'name' and 'city' columns.
- The 'age' column should contain only positive integers.
- The 'weight' column should contain values between 50 and 100.
- The 'height' column should contain values between 150 and 200.
- The 'income' column should contain values greater than 2000.
- The 'job' column should contain only 'engineer', 'teacher', or 'secretary'.
- The 'country' column should contain only 'Scotland', 'USA', or 'France'.
"""

import pandas as pd

def construct_dataframe(data):
    # Create a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Apply additional constraints
    df = df.drop_duplicates(subset='name')
    df = df[df['age'] > 0]
    df = df[(df['weight'] >= 50) & (df['weight'] <= 100)]
    df = df[(df['height'] >= 150) & (df['height'] <= 200)]
    df = df[df['income'] > 2000]
    df = df[df['job'].isin(['engineer', 'teacher', 'secretary'])]
    df = df.drop_duplicates(subset='city')
    df = df[df['country'].isin(['Scotland', 'USA', 'France'])]
    
    return df