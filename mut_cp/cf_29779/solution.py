"""
ORIGINAL QUESTION:
Write a function `mutation_summary(df)` that takes a pandas DataFrame `df` as input, where `df` contains 'mutation_type' and 'mutation_rate' columns, and 'mutation_type' only contains the values 'cpg', 'transition', or 'transversion'. The function should return a dictionary containing the total number of mutations, the average mutation rate for each mutation type, and the mutation type with the highest mutation rate.
"""

import pandas as pd

def mutation_summary(df):
    summary = {}
    
    # Total number of mutations
    total_mutations = len(df)
    summary['total_mutations'] = total_mutations
    
    # Average mutation rate for each mutation type
    avg_mutation_rate = df.groupby('mutation_type')['mutation_rate'].mean().to_dict()
    summary['average_mutation_rate'] = avg_mutation_rate
    
    # Mutation type with the highest mutation rate
    highest_mutation_type = max(avg_mutation_rate, key=avg_mutation_rate.get)
    summary['highest_mutation_rate_type'] = highest_mutation_type
    
    return summary