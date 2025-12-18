"""
QUESTION:
Write a function `choose_regression_model` that determines whether to use a Poisson or Quasi-Poisson regression model for a given dataset with rate data and a benchmark rate. The function should take into account the presence or absence of overdispersion in the data and the data type of the outcome variable.
"""

def choose_regression_model(data, benchmark_rate):
    """
    This function determines whether to use a Poisson or Quasi-Poisson regression model 
    based on the presence or absence of overdispersion in the data and the data type of 
    the outcome variable.

    Args:
        data (list): A list of rate data.
        benchmark_rate (float): The benchmark rate.

    Returns:
        str: The recommended regression model.
    """

    # Check for overdispersion in the data
    variance = sum((x - sum(data) / len(data)) ** 2 for x in data) / len(data)
    mean = sum(data) / len(data)

    # If the data is overdispersed, recommend Quasi-Poisson regression
    if variance > mean:
        return "Quasi-Poisson regression"

    # If the data is not overdispersed and the outcome variable is counts, recommend Poisson regression
    elif all(isinstance(x, int) for x in data):
        return "Poisson regression"

    # If the data is not overdispersed but the outcome variable is not counts, recommend Quasi-Poisson regression
    else:
        return "Quasi-Poisson regression"