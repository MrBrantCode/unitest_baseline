"""
QUESTION:
Write a function `assign_titles(data)` that takes a pandas DataFrame `data` as input with a column "Name" containing names of passengers. The function should add a new column "Title" to the DataFrame and assign numerical titles based on the following rules:
- "Mrs": 1.0
- "Miss": 2.0
- "Master": 3.0
- "Don": 4.0
- "Rev": 5.0
- "Dr": 6.0
- "Mme": 7.0
- "Ms": 8.0

If a name does not match any of the specified titles, the corresponding value in the "Title" column should be NaN.
"""

import pandas as pd

def assign_titles(data):
    data["Title"] = None  # Create a new column "Title" and initialize with None
    data.loc[data["Name"].str.contains("Mrs"), "Title"] = 1.0
    data.loc[data["Name"].str.contains("Miss"), "Title"] = 2.0
    data.loc[data["Name"].str.contains("Master"), "Title"] = 3.0
    data.loc[data["Name"].str.contains("Don"), "Title"] = 4.0
    data.loc[data["Name"].str.contains("Rev"), "Title"] = 5.0
    data.loc[data["Name"].str.contains("Dr"), "Title"] = 6.0
    data.loc[data["Name"].str.contains("Mme"), "Title"] = 7.0
    data.loc[data["Name"].str.contains("Ms"), "Title"] = 8.0
    return data