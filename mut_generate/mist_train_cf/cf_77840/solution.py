"""
QUESTION:
Create a function named `calculate_bmi_bsa` that takes a pandas DataFrame as input, adds two new columns 'BMI' and 'BSA' to the DataFrame, and returns the modified DataFrame. The DataFrame is expected to have columns 'weight(kg)' and 'height(cm)'. The 'BMI' column should be calculated using the formula weight(kg)/(height(m))^2 and the 'BSA' column should be calculated using the Du Bois formula: 0.007184 * Weight^0.425 * Height^0.725. The height should be correctly transformed from cm to m before calculations.
"""

import pandas as pd

def calculate_bmi_bsa(df):
    """
    Calculate BMI and BSA from a pandas DataFrame.

    Parameters:
    df (pandas DataFrame): DataFrame containing 'weight(kg)' and 'height(cm)' columns.

    Returns:
    pandas DataFrame: DataFrame with additional 'BMI' and 'BSA' columns.
    """
    # Calculate BMI and BSA & create new columns
    df['BMI'] = df['weight(kg)'] / ((df['height(cm)'] / 100) ** 2)
    df['BSA'] = 0.007184 * df['weight(kg)'] ** 0.425 * (df['height(cm)'] / 100) ** 0.725
    return df