"""
QUESTION:
Implement the function `preprocess_data(db, temp)` that takes two pandas DataFrames `db` and `temp` as input. The function should perform the following operations: 
- Concatenate `temp` to `db` along the rows.
- Reset the index of the resulting DataFrame and drop the previous index.
- Identify the indices of rows with missing values in the `npl` column and remove these rows from the DataFrame.
- Reset the indices of the resulting DataFrame. 
The function should return the preprocessed DataFrame. 

Function Signature: `def preprocess_data(db: pd.DataFrame, temp: pd.DataFrame) -> pd.DataFrame:`
"""

import pandas as pd

def preprocess_data(db: pd.DataFrame, temp: pd.DataFrame) -> pd.DataFrame:
    # Concatenate temp to db along the rows
    db = pd.concat([db, temp], axis=0)

    # Reset index and drop the previous index
    db.reset_index(inplace=True, drop=True)

    # Get indices of rows with missing npl
    missing_npl_idx = db[db.npl.isna()].index

    # Remove rows with missing npl
    db.drop(missing_npl_idx, axis=0, inplace=True)

    # Reset indices
    db.reset_index(inplace=True, drop=True)

    return db