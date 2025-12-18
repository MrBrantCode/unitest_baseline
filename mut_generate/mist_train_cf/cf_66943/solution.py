"""
QUESTION:
Write a function called `survey_analysis` that takes a pandas DataFrame as input, where the DataFrame contains information about software developers, including their preferred programming language, years of experience, industry, and frequency of language usage. The function should return the most popular language and the average years of experience per language. 

The input DataFrame should have columns 'Language', 'Experience', 'Industry', and 'Usage(hours/week)'. The function should use pandas for data analysis and matplotlib for data visualization. 

Note that this is a simplified version of a comprehensive survey analysis and may need to be tailored to specific needs.
"""

import pandas as pd

def survey_analysis(df):
    """
    Analyze a software developer survey DataFrame.

    Parameters:
    df (pandas DataFrame): A DataFrame with columns 'Language', 'Experience', 'Industry', and 'Usage(hours/week)'.

    Returns:
    tuple: A tuple containing the most popular language and the average years of experience per language.
    """
    # Count the popularity of languages
    languages_count = df['Language'].value_counts()

    # Find most popular language
    most_popular = languages_count.idxmax()

    # Compute average experience per language
    avg_experience = df.groupby('Language')['Experience'].mean()

    return most_popular, avg_experience