"""
QUESTION:
Write a function named `process_genomic_data` that takes two DataFrames, `gtf` and `lincRNAIDs`, as input. Filter the `gtf` DataFrame to include only rows where the feature is 'exon', the seqname is not 'chrM', and the gene_type is 'specific_gene_type'. Then, merge the filtered `gtf` DataFrame with the `lincRNAIDs` DataFrame based on a common column. The function should return the merged DataFrame after any necessary data cleaning or manipulation.
"""

import pandas as pd

def process_genomic_data(gtf, lincRNAIDs):
    """
    This function processes genomic data by filtering and merging two DataFrames.
    
    Parameters:
    gtf (DataFrame): The DataFrame containing genomic data.
    lincRNAIDs (DataFrame): The DataFrame containing lincRNA IDs.
    
    Returns:
    DataFrame: The merged DataFrame after filtering and data cleaning.
    """
    
    # Filter the gtf DataFrame to include only rows where the feature is 'exon', 
    # the seqname is not 'chrM', and the gene_type is 'specific_gene_type'
    exons = gtf[(gtf.feature == 'exon') & (gtf.seqname != 'chrM') & (gtf.gene_type == 'specific_gene_type')]
    
    # Merge the filtered gtf DataFrame with the lincRNAIDs DataFrame based on a common column
    merged_data = pd.merge(exons, lincRNAIDs, how='inner', on='common_column')
    
    # Perform any necessary data cleaning or manipulation
    # For example, drop any duplicate rows
    final_output = merged_data.drop_duplicates()
    
    return final_output