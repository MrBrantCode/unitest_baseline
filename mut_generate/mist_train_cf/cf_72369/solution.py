"""
QUESTION:
Write a function `estimate_policy_effect` to reorganize a dataset for a difference-in-differences analysis. The dataset contains information about farmers' lands, including the farmer's ID, village, land size, and treatment status (treated or control). Some farmers have lands in both treatment and control villages. The function should categorize these farmers as a separate group ("Both Treated and Control") and compare the changes among treated farmers, controlled farmers, and farmers with lands in both groups. The function should return a pandas DataFrame with the reorganized dataset.
"""

import pandas as pd

def estimate_policy_effect(df):
    """
    Reorganize a dataset for a difference-in-differences analysis.
    
    This function categorizes farmers with lands in both treatment and control villages 
    as a separate group ("Both Treated and Control") and compares the changes among 
    treated farmers, controlled farmers, and farmers with lands in both groups.
    
    Parameters:
    df (pd.DataFrame): The input dataset containing information about farmers' lands.
    
    Returns:
    pd.DataFrame: A pandas DataFrame with the reorganized dataset.
    """
    
    # Create a dictionary to store the groups for each farmer
    farmer_groups = {}
    
    # Iterate over each row in the dataset
    for index, row in df.iterrows():
        farmer_id = row['Farmer_ID']
        village = row['Village']
        treatment_status = row['Treatment_Status']
        
        # If the farmer is already in the dictionary, update their group
        if farmer_id in farmer_groups:
            if farmer_groups[farmer_id] == 'Treated' and treatment_status == 'Control':
                farmer_groups[farmer_id] = 'Both Treated and Control'
            elif farmer_groups[farmer_id] == 'Control' and treatment_status == 'Treated':
                farmer_groups[farmer_id] = 'Both Treated and Control'
        # If the farmer is not in the dictionary, add them
        else:
            farmer_groups[farmer_id] = treatment_status
    
    # Create a new column 'Group' in the dataset based on the farmer groups
    df['Group'] = df['Farmer_ID'].apply(lambda x: farmer_groups[x])
    
    return df