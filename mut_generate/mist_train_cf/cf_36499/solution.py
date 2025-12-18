"""
QUESTION:
Write a Python function named `analyze_connectors` that takes the path to a CSV file containing connector data as input and returns a dictionary containing the total number of connectors, unique types of connectors, and the average price of the connectors. The function should assume that the CSV file has columns named 'type' and 'price'. The dictionary should have the following key-value pairs: 
- "total_connectors": total number of connectors 
- "unique_types": list of unique types of connectors
- "average_price": average price of the connectors
"""

import pandas as pd

def analyze_connectors(connector_path: str) -> dict:
    # Load the CSV file into a pandas DataFrame
    connectors = pd.read_csv(connector_path)

    # Calculate the total number of connectors in the dataset
    total_connectors = len(connectors)

    # Identify the unique types of connectors available in the dataset
    unique_types = connectors['type'].unique().tolist()

    # Determine the average price of the connectors
    average_price = connectors['price'].mean()

    # Return the results as a dictionary
    analysis_results = {
        "total_connectors": total_connectors,
        "unique_types": unique_types,
        "average_price": average_price
    }

    return analysis_results