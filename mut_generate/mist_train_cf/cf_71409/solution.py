"""
QUESTION:
Write a function named `equity_distribution` to determine the initial investment distribution in two classes of equities with annual yields of 7% and 8%, given an initial capital of $500 and a cumulative return of $36. The function should return the amount invested in the 7% and 8% yield equities.
"""

def equity_distribution(capital, cumulative_return, yield1, yield2):
    """
    This function determines the initial investment distribution in two classes of equities with given yields.

    Args:
        capital (float): The initial capital.
        cumulative_return (float): The cumulative return.
        yield1 (float): The annual yield of the first class of equities.
        yield2 (float): The annual yield of the second class of equities.

    Returns:
        tuple: A tuple containing the amount invested in the first and second class of equities.
    """

    # Denote the money invested into the first class of equities as x dollars
    x = (cumulative_return - yield2 * capital) / (yield1 - yield2)

    # Calculate the amount invested in the second class of equities
    y = capital - x

    return x, y