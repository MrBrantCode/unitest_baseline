"""
QUESTION:
Write a function called `align_curves` that adjusts for the difference in settlement dates between an interest rate swap (IRS) curve and an overnight index swap (OIS) curve. The IRS curve has a same-day settlement, while the OIS curve has a one-day settlement delay. The function should be able to adjust the settlement dates of the curves to ensure they start accruing interest at the same time.
"""

from datetime import timedelta

def align_curves(irs_curve, ois_curve):
    """
    Aligns the settlement dates of an interest rate swap (IRS) curve and an overnight index swap (OIS) curve.

    Args:
        irs_curve (list of tuples): A list of tuples containing the dates and rates of the IRS curve.
        ois_curve (list of tuples): A list of tuples containing the dates and rates of the OIS curve.

    Returns:
        list of tuples: The adjusted OIS curve with settlement dates shifted forward by one day to match the IRS curve.
    """
    adjusted_ois_curve = [(date + timedelta(days=1), rate) for date, rate in ois_curve]
    return adjusted_ois_curve