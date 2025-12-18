"""
QUESTION:
Implement the `calculate_metrics` function to calculate performance metrics for a predictive model. The function takes two pandas DataFrames `df_gs` and `df_pred` as input, each containing `clinical_case` and `code` columns. 

The function should calculate the following metrics: 
- Pred_Pos_per_cc: Number of unique predicted codes per clinical case
- Pred_Pos: Total number of unique predicted codes across all clinical cases
- GS_Pos_per_cc: Number of unique gold standard codes per clinical case
- GS_Pos: Total number of unique gold standard codes across all clinical cases
- TP_per_cc: True positives per clinical case, where true positives are the number of codes that appear in both the predicted and gold standard sets for each clinical case

The function should return these metrics as a dictionary.
"""

import pandas as pd

def calculate_metrics(df_gs, df_pred):
    # Calculate Pred_Pos_per_cc
    Pred_Pos_per_cc = df_pred.drop_duplicates(subset=['clinical_case', 'code']).groupby("clinical_case")["code"].count()
    
    # Calculate Pred_Pos
    Pred_Pos = df_pred.drop_duplicates(subset=['clinical_case', 'code']).shape[0]
    
    # Calculate GS_Pos_per_cc
    GS_Pos_per_cc = df_gs.drop_duplicates(subset=['clinical_case', 'code']).groupby("clinical_case")["code"].count()
    
    # Calculate GS_Pos
    GS_Pos = df_gs.drop_duplicates(subset=['clinical_case', 'code']).shape[0]
    
    # Calculate TP_per_cc
    cc = set(df_gs.clinical_case.tolist())
    TP_per_cc = {}
    for c in cc:
        pred = set(df_pred.loc[df_pred['clinical_case']==c,'code'].values)
        gs = set(df_gs.loc[df_gs['clinical_case']==c,'code'].values)
        TP_per_cc[c] = len(pred.intersection(gs))
    
    # Return the metrics as a dictionary
    metrics = {
        'Pred_Pos_per_cc': Pred_Pos_per_cc.to_dict(),
        'Pred_Pos': Pred_Pos,
        'GS_Pos_per_cc': GS_Pos_per_cc.to_dict(),
        'GS_Pos': GS_Pos,
        'TP_per_cc': TP_per_cc
    }
    return metrics