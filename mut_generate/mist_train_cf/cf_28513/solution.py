"""
QUESTION:
Implement a function `rank_and_aggregate_results(results_agg)` that takes a DataFrame `results_agg` with columns `DATASET`, `RANK`, and `FRAMEWORK` and returns a DataFrame. The function should perform the following operations: 
1. Extract unique dataset names from `results_agg`. 
2. Rank the results by `DATASET` and `RANK`, and select the top two rows for each dataset. 
3. For each dataset, count the occurrences of the top-ranked framework (rank=1) and add this count to the result as `rank=1_count`. 
4. For each dataset, count the occurrences of the second-ranked frameworks (rank=2) and add this count to the result as `rank=2_count`. 

Note: The returned DataFrame should contain all columns from the original DataFrame plus the additional `rank=1_count` and `rank=2_count` columns.
"""

import pandas as pd

def rank_and_aggregate_results(results_agg):
    valid_tasks = list(results_agg['DATASET'].unique())

    # Rank the results
    results_ranked = results_agg.sort_values(by=['DATASET', 'RANK']).groupby('DATASET').head(2)

    # Count occurrences of rank=1 frameworks
    rank_1_count = results_ranked[results_ranked['RANK'] == 1]['FRAMEWORK'].value_counts().reset_index()
    rank_1_count.columns = ['FRAMEWORK', 'rank=1_count']
    results_ranked = results_ranked.merge(rank_1_count, on='FRAMEWORK', how='left').fillna(0)

    # Count occurrences of rank=2 frameworks
    rank_2_count = results_ranked[(results_ranked['RANK'] > 1) & (results_ranked['RANK'] <= 2)]['FRAMEWORK'].value_counts().reset_index()
    rank_2_count.columns = ['FRAMEWORK', 'rank=2_count']
    results_ranked = results_ranked.merge(rank_2_count, on='FRAMEWORK', how='left').fillna(0)

    results_ranked['rank=1_count'] = results_ranked['rank=1_count'].astype(int)
    results_ranked['rank=2_count'] = results_ranked['rank=2_count'].astype(int)

    return results_ranked