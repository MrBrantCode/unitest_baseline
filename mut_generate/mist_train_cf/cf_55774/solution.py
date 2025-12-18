"""
QUESTION:
Create a function `generate_profiles` that takes a list of JSON objects as input and returns a DataFrame. The JSON objects should contain the keys 'name', 'age', 'interests', 'profession', and 'education'. The function should calculate the average age for each unique profession and define functions to filter profiles based on age, profession, and interests. The filtering functions should be named `filter_age`, `filter_profession`, and `filter_interest` respectively. 

The input JSON data will be in the following format:
{
    "name": string,
    "age": int,
    "interests": list of strings,
    "profession": string,
    "education": string
}
"""

import pandas as pd

def generate_profiles(json_data):
    # Convert JSON to DataFrame
    df = pd.DataFrame(json_data)

    # Calculate average age for each unique profession
    average_age = df.groupby('profession')['age'].mean()

    # Functions to filter profiles
    def filter_age(age):
        return df[df['age'] == age]

    def filter_profession(profession):
        return df[df['profession'] == profession]

    def filter_interest(interest):
        return df[df['interests'].apply(lambda interests: interest in interests)]

    return df, average_age, filter_age, filter_profession, filter_interest