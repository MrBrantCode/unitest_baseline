"""
QUESTION:
Implement a function `replicate_and_store` that replicates a given 2D array `blankMap` a specified number of times `genomeLength` and stores the copies in a list of pandas DataFrames. Each copy must be an independent copy of the original `blankMap`. The function takes `blankMap` and `genomeLength` as input and returns a list of pandas DataFrames.

Function Signature: `def replicate_and_store(blankMap: List[List[int]], genomeLength: int) -> List[pd.DataFrame]`
"""

import pandas as pd
from typing import List

def replicate_and_store(blankMap: List[List[int]], genomeLength: int) -> List[pd.DataFrame]:
    map_genes = []
    for i in range(genomeLength):
        map_genes.append(pd.DataFrame(data=blankMap).copy(deep=True))
    return map_genes