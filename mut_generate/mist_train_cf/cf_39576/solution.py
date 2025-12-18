"""
QUESTION:
Implement a function `calculate_FDR` that takes a list of p-values, a cutoff value `mEvalueCutoff`, and a desired false discovery rate `mFDR` as input, and returns the calculated false discovery rate (FDR) using the formula FDR = (mFDR * sum(p_values <= mEvalueCutoff)) / max(1, sum(p_values <= mEvalueCutoff)).
"""

def calculate_FDR(p_values, mEvalueCutoff, mFDR):
    num_rejected = sum(p <= mEvalueCutoff for p in p_values)
    total_rejected = max(1, num_rejected)
    FDR = (mFDR * num_rejected) / total_rejected
    return FDR