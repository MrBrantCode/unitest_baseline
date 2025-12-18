"""
QUESTION:
Implement a Python class named `FFMirror` that inherits from `BaseInterface` and `GroupDevice`. The `FFMirror` class should have a constructor that takes a single parameter `prefix` of type `str`, representing the base PV for the mirror, and initializes the mirror with this base PV.
"""

def entrance(prefix: str):
    """
    Fixed Focus Kirkpatrick-Baez Mirror.

    1st gen Toyama designs with LCLS-II Beckhoff motion architecture.

    Parameters
    ----------
    prefix : str
        Base PV for the mirror.

    Returns
    -------
    None
    """
    prefix = prefix
    return prefix