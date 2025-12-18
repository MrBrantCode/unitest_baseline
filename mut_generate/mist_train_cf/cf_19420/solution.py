"""
QUESTION:
Compute the function `bayes_rain_probability` that calculates the probability of rain given that the grass is wet. The function should take three parameters: `prob_grass_wet_given_rain` (the probability of the grass being wet when it rains), `prob_rain` (the overall probability of rain), and `prob_grass_wet` (the overall probability of the grass being wet). The function should return the calculated probability and use a constant amount of additional memory.
"""

def bayes_rain_probability(prob_grass_wet_given_rain, prob_rain, prob_grass_wet):
    """
    Compute the probability of rain given that the grass is wet using Bayes' theorem.

    Parameters:
    prob_grass_wet_given_rain (float): The probability of the grass being wet when it rains.
    prob_rain (float): The overall probability of rain.
    prob_grass_wet (float): The overall probability of the grass being wet.

    Returns:
    float: The calculated probability of rain given that the grass is wet.
    """
    return (prob_grass_wet_given_rain * prob_rain) / prob_grass_wet