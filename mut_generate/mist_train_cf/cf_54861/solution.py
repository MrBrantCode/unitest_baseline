"""
QUESTION:
Write a function `cds_pricing` that takes in a CDS spread, a recovery rate used for calibration, and a recovery rate used for pricing. The function should return the price of the CDS using the given recovery rates. The function should consider the case where the recovery rates used for calibration and pricing are different.
"""

def cds_pricing(spread, recovery_rate_calibration, recovery_rate_pricing):
    """
    Calculate the price of a Credit Default Swap (CDS) using given recovery rates.

    Args:
    spread (float): The CDS spread.
    recovery_rate_calibration (float): The recovery rate used for calibration.
    recovery_rate_pricing (float): The recovery rate used for pricing.

    Returns:
    float: The price of the CDS.
    """
    # Implementation based on the Hull theory
    # For simplicity, let's assume the CDS price is proportional to the spread and inversely proportional to the difference between the two recovery rates
    # This is a simplified example and actual implementation may vary based on the specific requirements and models used
    return spread / (1 - recovery_rate_pricing) * (1 - recovery_rate_calibration)