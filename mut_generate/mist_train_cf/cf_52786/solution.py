"""
QUESTION:
Create a function named `transform_values` that takes a pandas DataFrame as input and modifies its values based on the frequency of occurrence in each column. For the 'Qu1' column, replace values with 'other' if they appear less than 3 times, and for the 'Qu2' and 'Qu3' columns, replace values with 'other' if they appear less than 2 times. Return the modified DataFrame.
"""

def transform_values(df):
    result = df.copy()
    result['Qu1'] = ['other' if (df['Qu1'].values == element).sum() < 3 else element for element in df['Qu1'].values]
    result['Qu2'] = ['other' if (df['Qu2'].values == element).sum() < 2 else element for element in df['Qu2'].values]
    result['Qu3'] = ['other' if (df['Qu3'].values == element).sum() < 2 else element for element in df['Qu3'].values]
    return result