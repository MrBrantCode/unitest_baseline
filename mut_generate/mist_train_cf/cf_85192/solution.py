"""
QUESTION:
Write a function `mocking_approach` that returns the preferred approach when unit testing, whether to use mock frameworks or test stubs, considering factors like complexity, control, and maintainability.
"""

def mocking_approach(complexity, control, maintainability):
    """
    Returns the preferred approach when unit testing, whether to use mock frameworks or test stubs.

    Parameters:
    complexity (str): Level of complexity ('high', 'low')
    control (str): Level of control needed ('high', 'low')
    maintainability (str): Level of maintainability required ('high', 'low')

    Returns:
    str: Preferred approach ('mock frameworks' or 'test stubs')
    """

    # Determine the preferred approach based on the given factors
    if complexity == 'high' or control == 'high':
        # If complexity or control is high, use mock frameworks
        return 'mock frameworks'
    elif maintainability == 'high':
        # If maintainability is high, use test stubs
        return 'test stubs'
    else:
        # Otherwise, use test stubs as a default
        return 'test stubs'