"""
QUESTION:
Implement the function `generate_performance_summary(tr_avg_performances, vl_avg_performances, vl_std_performances)` to calculate the mean and standard deviation of the performance metrics for training and validation sets, excluding the last center. The function should take three lists of performance metrics as input: `tr_avg_performances` for training, `vl_avg_performances` for validation averages, and `vl_std_performances` for validation standard deviations, and return a dictionary containing the summary report with keys 'tr_mean_dice', 'tr_std_dice', 'vl_mean_dice', and 'vl_std_dice'.
"""

import numpy as np

def generate_performance_summary(tr_avg_performances, vl_avg_performances, vl_std_performances):
    tr_mean_dice = np.mean(tr_avg_performances[:-1])
    tr_std_dice = np.std(tr_avg_performances[:-1])
    
    vl_mean_dice = np.mean(vl_avg_performances[:-1])
    vl_std_dice = np.mean(vl_std_performances[:-1])  # corrected this line
    
    summary_report = {
        'tr_mean_dice': tr_mean_dice,
        'tr_std_dice': tr_std_dice,
        'vl_mean_dice': vl_mean_dice,
        'vl_std_dice': vl_std_dice
    }
    
    return summary_report