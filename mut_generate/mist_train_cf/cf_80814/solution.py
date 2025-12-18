"""
QUESTION:
Create a function named `calculate_net_margin` that calculates the net margin according to the standardized rule set by BCBS 261. The function should take two parameters: `NGR` (the ratio of Net to gross Market value of the underlying trades in the portfolio) and `gross_margin`. The function should return the calculated net margin, where Net Margin = (0.40 + 0.60 * NGR) * Gross Margin.
"""

def calculate_net_margin(NGR, gross_margin):
    """
    Calculate the net margin according to the standardized rule set by BCBS 261.

    Parameters:
    NGR (float): The ratio of Net to gross Market value of the underlying trades in the portfolio.
    gross_margin (float): The gross margin of the portfolio.

    Returns:
    float: The calculated net margin.
    """
    return (0.40 + 0.60 * NGR) * gross_margin