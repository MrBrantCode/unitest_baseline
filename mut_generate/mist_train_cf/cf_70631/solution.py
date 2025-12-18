"""
QUESTION:
Create a function `transform_df` that takes a DataFrame with columns 'name', 'weight(kg)', and 'height(cm)' as input. The function should return the DataFrame with two additional columns 'BMI' and 'BSA' calculated from the existing 'weight(kg)' and 'height(cm)' columns using the formulas: BMI = weight(kg) / (height(m))^2 and BSA = 0.007184 * (weight(kg)^(0.425)) * (height(cm)^(0.725)). Additionally, the function should include two more columns 'weight(lbs)' and 'height(inch)' with the converted values from metric units to imperial units using the formulas: weight(lbs) = weight(kg) * 2.20462 and height(inch) = height(cm) / 2.54. Ensure accuracy up to 2 decimal places and do not use any pre-built libraries for unit conversion.
"""

import pandas as pd

def transform_df(df):
    # Calculate BMI and BSA
    df['BMI'] = df.apply(lambda row: round(row['weight(kg)'] / ((row['height(cm)'] / 100) ** 2), 2), axis=1)
    df['BSA'] = df.apply(lambda row: round(0.007184 * (row['weight(kg)'] ** 0.425) * (row['height(cm)'] ** 0.725), 2), axis=1)

    # Convert weight and height from metric to imperial units
    df['weight(lbs)'] = df['weight(kg)'].apply(lambda x: round(x * 2.20462, 2))
    df['height(inch)'] = df['height(cm)'].apply(lambda x: round(x / 2.54, 2))

    return df