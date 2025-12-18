"""
QUESTION:
Calculate the Hedges' g for a meta-analysis of studies that report outcomes in different units. The studies compare fine roots in compacted and non-compacted soil, but report fine roots as either biomass or number per surface unit. Is it scientifically valid to combine these studies into a single database and use Hedges' g as the effect size measure, or should the data be separated into two databases based on the type of outcome reported?
"""

def hedges_g(m1, m2, sd1, sd2, n1, n2):
    """
    Calculate the Hedges' g for a meta-analysis.

    Args:
        m1 (float): The mean of the first group.
        m2 (float): The mean of the second group.
        sd1 (float): The standard deviation of the first group.
        sd2 (float): The standard deviation of the second group.
        n1 (int): The sample size of the first group.
        n2 (int): The sample size of the second group.

    Returns:
        float: The Hedges' g value.
    """
    # Calculate the pooled standard deviation
    sp = ((n1 - 1) * sd1**2 + (n2 - 1) * sd2**2) / (n1 + n2 - 2)
    sp = sp**0.5

    # Calculate the Hedges' g
    g = (m1 - m2) / sp
    g = g * (1 - 3 / (4 * (n1 + n2) - 9))

    return g