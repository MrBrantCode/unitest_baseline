"""
QUESTION:
Implement a function `calculate_ncc(patchA, patchB)` that calculates the normalized cross-correlation (NCC) between two 3D arrays `patchA` and `patchB`. The NCC is calculated using the formula: 
\[ NCC = \frac{\sum_{i=1}^{n}(patchA_i - \bar{patchA})(patchB_i - \bar{patchB})}{\sqrt{\sum_{i=1}^{n}(patchA_i - \bar{patchA})^2} \cdot \sqrt{\sum_{i=1}^{n}(patchB_i - \bar{patchB})^2}} \]
where \( \bar{patchA} \) and \( \bar{patchB} \) are the means of `patchA` and `patchB` respectively, and \( n \) is the total number of elements in the patches.
"""

import numpy as np

def calculate_ncc(patchA, patchB):
    mean_patchA = np.mean(patchA)
    mean_patchB = np.mean(patchB)
    
    numerator = np.sum((patchA - mean_patchA) * (patchB - mean_patchB))
    denominator = np.sqrt(np.sum((patchA - mean_patchA)**2)) * np.sqrt(np.sum((patchB - mean_patchB)**2))
    
    ncc = numerator / denominator
    return ncc