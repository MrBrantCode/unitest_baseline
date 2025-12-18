"""
QUESTION:
Implement the function `calculate_fdr_ranking(p_values)` that takes a list of p-values and returns a list of the same length where each element represents the FDR ranking for the corresponding p-value. The FDR ranking should be calculated by sorting the p-values in ascending order, calculating the FDR for each p-value using the formula FDR = (p-value * total hypotheses) / (rank * total hypotheses), and then ranking the p-values based on their FDR values. The FDR ranking list should be 1-indexed, with lower FDR values indicating higher significance.
"""

def calculate_fdr_ranking(p_values):
    sorted_p_values = sorted(p_values)
    total_hypotheses = len(p_values)
    fdr_ranking = []

    for i, p_value in enumerate(p_values):
        rank = sorted_p_values.index(p_value) + 1
        fdr = (p_value * total_hypotheses) / (rank * total_hypotheses)
        fdr_ranking.append(fdr)

    # Rank the p-values based on FDR values
    ranked_indices = sorted(range(len(fdr_ranking)), key=lambda k: fdr_ranking[k])
    fdr_ranking = [ranked_indices.index(i) + 1 for i in range(len(p_values))]

    return fdr_ranking