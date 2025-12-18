"""
QUESTION:
Create a function `parse_json_to_dataframe` that takes a JSON object as input. The JSON object contains a list of people with their details. Parse the JSON object and store the data in a Pandas dataframe with the following columns: 'Name', 'Age', 'Street', 'City', 'State', and 'Country'. The 'Country' column should contain the country name of each individual. 

The input JSON object has the following structure:
- Each person has a 'Name', 'Age', and 'Address'.
- Each 'Address' has a 'Street', 'City', 'State', and 'Country'.
"""

import pandas as pd
import json

def parse_json_to_dataframe(json_data):
    """
    This function takes a JSON object as input, parses it and returns a Pandas dataframe.
    
    The JSON object should contain a list of people with their details.
    The function extracts 'Name', 'Age', 'Street', 'City', 'State', and 'Country' from each person's details.
    
    Parameters:
    json_data (str): A JSON object containing a list of people with their details.
    
    Returns:
    pd.DataFrame: A Pandas dataframe containing the extracted data.
    """
    
    # Load JSON data into a Python dictionary
    data = json.loads(json_data)
    
    # Extract required fields from the JSON dictionary
    records = []
    for person in data["people"]:
        name = person["Name"]
        age = person["Age"]
        street = person["Address"]["Street"]
        city = person["Address"]["City"]
        state = person["Address"]["State"]
        country = person["Address"]["Country"]
        records.append((name, age, street, city, state, country))
    
    # Create a Pandas dataframe from the extracted records
    df = pd.DataFrame(records, columns=["Name", "Age", "Street", "City", "State", "Country"])
    
    return df