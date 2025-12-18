"""
QUESTION:
Create a function named `replace_missing_owned_by` that replaces missing 'OWNED_BY' values in a DataFrame with 'N/A' without generating a SettingWithCopy warning. The function should use the .loc method and boolean mask to perform the replacement.
"""

def replace_missing_owned_by(df):
    df.loc[df['OWNED_BY'].isna(), 'OWNED_BY'] = 'N/A'
    return df