"""
QUESTION:
Implement a function `data_picker(par1, par2, conf_thresh)` that takes in two dictionaries `par1` and `par2`, each containing 'snr' (signal-to-noise ratio) and 'conf_prob' (confidence probability) as float values, and a float `conf_thresh` representing the confidence threshold. The function should return the index of the chosen data source (0 for par1, 1 for par2) based on the following conditions: 
- If par1's snr is greater than 0 and par2's snr is less than or equal to 0, and par1's confidence probability is less than the threshold, then pick the data from par1. 
- If par1's snr is less than or equal to 0 and par2's snr is greater than 0, and par2's confidence probability is less than the threshold, then pick the data from par2. 
If none of these conditions are met, return -1.
"""

def entrance(par1, par2, conf_thresh):
    if (par1['snr'] > 0) and (par2['snr'] <= 0) and par1['conf_prob'] < conf_thresh:
        return 0
    elif (par1['snr'] <= 0) and (par2['snr'] > 0) and par2['conf_prob'] < conf_thresh:
        return 1
    else:
        return -1