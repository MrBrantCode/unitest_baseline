"""
QUESTION:
Write a function `compute_averages` that takes in a list of pandas dataframes `temp_veg_dfs`, a dictionary `spatial_prefix_map` mapping spatial prefixes to a list of regions, a list of treatment options `treatment_options`, and a list of scenarios `scenarios`. The function should return a nested dictionary containing the average temperature for each combination of spatial prefix, treatment, and scenario. The average temperature should be rounded to 2 decimal places, and if a combination does not have any data, the average temperature should be considered as 0.00. 

The input parameters have the following restrictions:
- 1 <= len(temp_veg_dfs) <= 100
- 1 <= len(spatial_prefix_map) <= 100
- 1 <= len(treatment_options) <= 10
- 1 <= len(scenarios) <= 5 

The structure of the output dictionary should be as follows:
```
{
    spatial_prefix_1: {
      treatment_1: {
        scenario_1: average_temp_1,
        scenario_2: average_temp_2,
        ...
      },
      treatment_2: {
        scenario_1: average_temp_3,
        scenario_2: average_temp_4,
        ...
      },
      ...
    },
    spatial_prefix_2: {
      ...
    },
    ...
  }
```
"""

import pandas as pd
from typing import List, Dict

def compute_averages(temp_veg_dfs: List[pd.DataFrame], spatial_prefix_map: Dict[str, List[str]], treatment_options: List[str], scenarios: List[str]) -> Dict[str, Dict[str, Dict[str, float]]]:
    result = {}
    for spatial_prefix, regions in spatial_prefix_map.items():
        result[spatial_prefix] = {}
        for treatment in treatment_options:
            result[spatial_prefix][treatment] = {}
            for scenario in scenarios:
                total_temp = 0
                count = 0
                for region in regions:
                    for df in temp_veg_dfs:
                        if region in df.columns:
                            total_temp += df[region].mean()
                            count += 1
                result[spatial_prefix][treatment][scenario] = round(total_temp / count, 2) if count > 0 else 0.00
    return result