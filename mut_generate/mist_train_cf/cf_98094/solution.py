"""
QUESTION:
Develop a Python function named `rank_features` that takes a CSV file path `survey_data` as input, representing a table of survey results with columns for 'Important', 'Somewhat important', and 'Not important' customer ratings for various features. The function should return a list of features ordered by the percentage of customers who rated them as 'Important' in descending order.
"""

import pandas as pd

def rank_features(survey_data):
    df = pd.read_csv(survey_data)
    total_customers = df[['Important', 'Somewhat important', 'Not important']].sum().sum()
    df_percent = df[['Important', 'Somewhat important', 'Not important']].apply(lambda x: x/total_customers*100)
    df_ranked = df_percent.sort_values(by='Important', ascending=False)
    return df_ranked.index.tolist()