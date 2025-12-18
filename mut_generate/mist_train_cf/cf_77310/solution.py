"""
QUESTION:
Create a function called `expected_strangle_return` that takes as input the change in implied volatility (`delta_iv`), the realized volatility (`rv`), the vega of the options (`vega`), and the premium paid for the strangle (`premium`). Return the estimated expected return of a strangle. The function should assume a symmetric strangle with the same number of contracts for puts and calls and consider the difference between the implied volatility of puts and calls due to skew. The function should not actually calculate the vega, delta_iv, or rv, but rather use the provided values as inputs.
"""

def expected_strangle_return(delta_iv, rv, vega, premium):
    """
    Estimate the expected return of a strangle.

    Args:
    delta_iv (float): The change in implied volatility.
    rv (float): The realized volatility.
    vega (float): The vega of the options.
    premium (float): The premium paid for the strangle.

    Returns:
    float: The estimated expected return of a strangle.
    """
    return vega * (delta_iv - rv) - premium