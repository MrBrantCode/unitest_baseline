"""
QUESTION:
Write a function called `extrapolate_volatility_surface` that takes in the listed options, forward price, and index options with longer maturity as inputs and returns an extrapolated volatility surface or term structure. Assume that the inputs are provided in a format that can be used directly in the function. The function should implement one or more of the following methods: linear extrapolation, curve fitting using polynomial regression, mixing different products, Black-Scholes-Merton model, stochastic volatility models, or using implied volatility surface models.
"""

def extrapolate_volatility_surface(listed_options, forward_price, index_options):
    # This function will implement one or more of the methods described in the problem statement
    # For simplicity, we will start with a basic linear extrapolation method

    # Assuming listed_options is a list of tuples containing strike price and volatility
    # And index_options is a list of tuples containing maturity and volatility

    # First, we sort the listed options by strike price
    listed_options.sort(key=lambda x: x[0])

    # Then, we calculate the slope of the existing volatility surface
    slope = (listed_options[-1][1] - listed_options[0][1]) / (listed_options[-1][0] - listed_options[0][0])

    # Now, we can extrapolate the volatility surface for the index options
    extrapolated_volatilities = []
    for maturity in index_options:
        # We use the slope to calculate the extrapolated volatility
        extrapolated_volatility = listed_options[-1][1] + slope * (maturity[0] - listed_options[-1][0])
        extrapolated_volatilities.append((maturity[0], extrapolated_volatility))

    return extrapolated_volatilities