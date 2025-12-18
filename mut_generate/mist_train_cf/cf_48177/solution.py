"""
QUESTION:
Function: Exclude Zero-Variance Features from Binary Classification Model

I have a binary classification problem with certain input categorical variables that have zero variance, meaning all records have the same value for these variables. Is it okay to exclude these variables during model building, or is it important to retain them? Are they contributing anything to the output, given there is no variation between output classes?
"""

def exclude_zero_variance_features(df):
    # Calculate variance of each column in the dataframe
    variance = df.var()
    
    # Identify columns with zero variance
    zero_variance_features = variance[variance == 0].index
    
    # Drop columns with zero variance
    df = df.drop(zero_variance_features, axis=1)
    
    return df