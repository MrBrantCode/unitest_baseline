"""
QUESTION:
Write a function `compare_regions` that takes in a DataFrame `data` and two region names `region` and `other_region`, where the DataFrame contains COVID-19 data with columns "Country/Region" and "Confirmed". The function should calculate the total number of confirmed cases for each region and return the region with the higher number of cases. The function should only rely on the given DataFrame and the region names, without using any external variables or modules other than pandas.
"""

import pandas as pd

def compare_regions(data, region, other_region):
    def get_total_cases(region_name):
        df = data[data["Country/Region"] == region_name]
        cases = df.groupby("Date")["Confirmed"].sum()
        return cases.sum()

    region_cases = get_total_cases(region)
    other_region_cases = get_total_cases(other_region)

    if region_cases > other_region_cases:
        return region
    else:
        return other_region