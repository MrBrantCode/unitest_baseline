"""
QUESTION:
Calculate the LIBOR rate for the stub period of a floating rate note, given the stub period duration and the regular interest period. The stub period is an irregular first or last interest period, and its duration may be shorter or longer than the regular interest period. The LIBOR rate for the stub period should be interpolated from the LIBOR rates of the closest surrounding maturities.
"""

def calculate_stub_libor(short_maturity_libor, long_maturity_libor, stub_duration, short_duration, long_duration):
    """
    Calculate the interpolated LIBOR rate for the stub period.

    Args:
        short_maturity_libor (float): The LIBOR rate for the shorter maturity.
        long_maturity_libor (float): The LIBOR rate for the longer maturity.
        stub_duration (float): The duration of the stub period.
        short_duration (float): The duration of the shorter maturity.
        long_duration (float): The duration of the longer maturity.

    Returns:
        float: The interpolated LIBOR rate for the stub period.
    """
    if short_duration == long_duration:
        return short_maturity_libor
    
    return short_maturity_libor + (long_maturity_libor - short_maturity_libor) * (stub_duration - short_duration) / (long_duration - short_duration)