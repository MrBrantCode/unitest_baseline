"""
QUESTION:
Write a Python function named `analyze_dataset` that takes the path to a CSV file as input. The function should use pandas to read the CSV file, handle missing values and duplicate records, and calculate the percentage of males and females in the dataset, as well as their average ages separately. The function should assume the CSV file has columns 'ID', 'Name', 'Gender', 'Age', 'City', and 'Salary'.
"""

import pandas as pd

def analyze_dataset(file_path):
    # Read the dataset from CSV file
    dataset = pd.read_csv(file_path)
    
    # Remove duplicate records
    dataset = dataset.drop_duplicates()
    
    # Remove rows with missing values
    dataset = dataset.dropna()
    
    # Calculate the percentage of males and females
    total_count = len(dataset)
    males_count = len(dataset[dataset['Gender'] == 'Male'])
    females_count = len(dataset[dataset['Gender'] == 'Female'])
    males_percentage = (males_count / total_count) * 100
    females_percentage = (females_count / total_count) * 100
    
    # Calculate the average age of males and females separately
    males_age_avg = dataset[dataset['Gender'] == 'Male']['Age'].mean()
    females_age_avg = dataset[dataset['Gender'] == 'Female']['Age'].mean()
    
    return {
        "males_percentage": males_percentage,
        "females_percentage": females_percentage,
        "males_age_avg": males_age_avg,
        "females_age_avg": females_age_avg
    }