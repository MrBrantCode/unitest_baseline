"""
QUESTION:
Create a function `compute_fdc` that takes in a numpy array `flows`, an integer `steps` with a default value of 500, a boolean `exceed` with a default value of True, and a string `col_name` with a default value of 'flow'. The function should compute the flow duration curve (FDC) and return a pandas DataFrame containing the sorted flow values and their corresponding exceedance probabilities. The FDC should be calculated by sorting the flow values in descending order and then calculating the exceedance probability for each flow value based on the input boolean flag `exceed`. If `exceed` is True, the exceedance probabilities should be calculated as the rank of each flow value divided by the total number of flow values plus one. If `exceed` is False, the exceedance probabilities should be linearly spaced from 0 to 1 with `steps` intervals.
"""

import numpy as np
import pandas as pd

def compute_fdc(flows: np.array, steps: int = 500, exceed: bool = True, col_name: str = 'flow') -> pd.DataFrame:
    sorted_flows = np.sort(flows)[::-1]
    
    if exceed:
        exceedance_probs = np.arange(1, len(sorted_flows) + 1) / (len(sorted_flows) + 1)
    else:
        exceedance_probs = np.linspace(0, 1, num=steps, endpoint=False)

    fdc_data = {col_name: sorted_flows[:len(exceedance_probs)], 'exceedance_prob': exceedance_probs}
    fdc_df = pd.DataFrame(fdc_data)

    return fdc_df