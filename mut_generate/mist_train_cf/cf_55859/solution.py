"""
QUESTION:
Write a function `handle_csv_file` that takes a CSV file name and a column name as input, reads the CSV file into a pandas DataFrame, cleans the data, and performs basic data analysis. 

The function should handle exceptions during file reading, remove columns with over 50% missing data, replace missing values in the remaining columns using their mean, and print a summary of the cleaned data. 

Additionally, it should call a function `group_and_calculate` that groups the data by the specified column name and calculates statistics like count, mean, max, and min for other numeric columns. 

Assume that the CSV file exists and has at least one numeric column.
"""

import pandas as pd
import numpy as np

def handle_csv_file(file_name, column_name):
    try:
        df = pd.read_csv(file_name)
    except Exception as e:
        print("Error occurred:", e)
        return

    # Remove columns with more than 50% missing data
    half_count = len(df) / 2
    df = df.dropna(thresh=half_count, axis=1)

    # Fill NA values with mean of the columns
    df = df.fillna(df.mean())

    print("Summary of the cleaned data:")
    print("Number of rows:", df.shape[0])
    print("Number of columns:", df.shape[1])
    print("Some basic statistics of the data:\n", df.describe())

    def group_and_calculate(df, column_name):
        try:
            grouped_data = df.groupby(column_name)

            # Calculate count, mean, max, min
            print("Grouped data statistics:")
            for column in df.select_dtypes(include=[np.number]):
                print("Column: ", column)
                print("Mean:\n", grouped_data[column].mean())
                print("Max:\n", grouped_data[column].max())
                print("Min:\n", grouped_data[column].min())
                print("Count:\n", grouped_data[column].count())
                print("----------------------------------")
        except KeyError as e:
            print("Column for grouping not found:", e)

    group_and_calculate(df, column_name)