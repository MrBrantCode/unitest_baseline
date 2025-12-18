"""
QUESTION:
Create a function `rank_features` that takes a CSV file `survey_data` as input, where each row represents a feature and columns 'Important', 'Somewhat important', and 'Not important' represent the number of customers who ranked each feature with that level of importance. The function should return a list of features ordered by the percentage of customers who rated them as 'Important' in descending order.
"""

import pandas as pd

def rank_features(survey_data):
    # read in the survey data table
    df = pd.read_csv(survey_data)

    # calculate the total number of customers who responded to the survey
    total_customers = df.sum().sum()

    # calculate the percentage of customers who rated each feature as important, somewhat important, and not important
    df_percent = df.apply(lambda x: x/total_customers*100)

    # rank the features by the percentage of customers who rated them as important, in descending order
    df_ranked = df_percent.sort_values(by='Important', ascending=False)

    # return the list of features ranked by importance
    return df_ranked.index.tolist()