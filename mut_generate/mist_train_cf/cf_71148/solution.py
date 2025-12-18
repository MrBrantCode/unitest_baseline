"""
QUESTION:
Write a proof that the smallest σ-field of subsets of a Borel set A of ℝ containing the open sets in A is {B ∈ ℬ(ℝ) | B ⊆ A}, where ℬ(ℝ) denotes the Borel σ-field on ℝ.
"""

def borel_subset(A, borel_sets):
    """
    Generate the smallest σ-field of subsets of a Borel set A of ℝ containing the open sets in A.

    Args:
    A (set): A Borel set of ℝ.
    borel_sets (list of sets): A list of Borel sets in ℝ.

    Returns:
    list of sets: The smallest σ-field of subsets of A containing the open sets in A.
    """
    sigma_field = [B & A for B in borel_sets if B.issubset(A)]
    return sigma_field