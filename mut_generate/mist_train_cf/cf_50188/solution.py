"""
QUESTION:
Write a function `calculate_breakeven_rate` that takes two arguments: `index_linked_bond_yield` and `benchmark_bond_yield`, which represent the yields of an index-linked bond and a conventional government bond with similar maturity, respectively. The function should return the breakeven inflation rate, calculated as the difference between the two yields. The yields are decimal values (e.g., -0.129875 for -0.129875%).
"""

def calculate_breakeven_rate(index_linked_bond_yield, benchmark_bond_yield):
    """
    Calculate the breakeven inflation rate as the difference between the yield of an index-linked bond and a conventional government bond with similar maturity.

    Args:
        index_linked_bond_yield (float): The yield of the index-linked bond.
        benchmark_bond_yield (float): The yield of the conventional government bond.

    Returns:
        float: The breakeven inflation rate.
    """
    return index_linked_bond_yield - benchmark_bond_yield