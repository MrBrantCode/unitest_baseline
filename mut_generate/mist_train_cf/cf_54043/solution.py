"""
QUESTION:
Write a function called `calculate_twr` that takes the returns of three consecutive sub-periods as input and returns the Time-Weighted Return (TWR) for the entire period. The function should accept the returns as decimal values (e.g., 5% = 0.05) and calculate the TWR using geometric linking.
"""

def calculate_twr(r1, r2, r3):
    """
    Calculate the Time-Weighted Return (TWR) for a given period.

    Args:
        r1 (float): The return of the first sub-period.
        r2 (float): The return of the second sub-period.
        r3 (float): The return of the third sub-period.

    Returns:
        float: The Time-Weighted Return (TWR) for the entire period.
    """
    twr = (1 + r1) * (1 + r2) * (1 + r3) - 1
    return twr