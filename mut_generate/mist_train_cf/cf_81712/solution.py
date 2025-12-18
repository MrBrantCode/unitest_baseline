"""
QUESTION:
Estimate the new DV01 of an at-the-money interest rate swap after a significant rate curve movement. 

Given: 
- Initial duration of the swap (e.g., 4.6 for a 5Y USD swap)
- Rate curve movement (e.g., 150-200bps)

Assumptions and Restrictions: 
- The swap's notional amount and exact starting rate are unknown.
- The rate curve movement is significant (more than 1%).
"""

def estimate_new_dv01(initial_duration, rate_curve_movement):
    """
    Estimates the new DV01 of an at-the-money interest rate swap after a significant rate curve movement.

    Args:
    initial_duration (float): Initial duration of the swap (e.g., 4.6 for a 5Y USD swap)
    rate_curve_movement (float): Rate curve movement (e.g., 150-200bps)

    Returns:
    float: The estimated new DV01 of the swap.
    """

    # Given the significant rate curve movement, the impact on DV01 will be less than the duration times the rate change due to convexity.
    # We use a basic approximation to estimate the new DV01.
    new_dv01 = initial_duration * rate_curve_movement * 0.01  # Convert rate curve movement from bps to percentage

    # A more accurate estimate would require calculating the DV01 at the new yield, which involves nonlinear computation.
    # However, this is a simplified approximation for demonstration purposes.

    return new_dv01