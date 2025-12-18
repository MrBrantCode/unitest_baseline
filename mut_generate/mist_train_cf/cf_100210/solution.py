"""
QUESTION:
Write a function called `adjust_probability` that takes a base probability and a dictionary of factors with their corresponding values as input, and returns the adjusted probability. The function should adjust the base probability based on the given factors and their values. Each factor in the dictionary should have a corresponding adjustment function that takes the factor's value as input and returns a multiplier to be applied to the base probability. The adjustment functions should be defined as follows: 
- If the factor is "weather", the function should return 1.2 if the value is "sunny", 0.8 if the value is "rainy", and 1.0 otherwise.
- If the factor is "user_input", the function should return 1.5 if the value is "yes" and 0.5 if the value is "no".
- Any other factor should return 1.0.
 
The function should apply the adjustments from each factor and return the final probability.
"""

def adjust_probability(base_probability, factors):
    """
    Adjusts the base probability based on the given factors and their values.

    Args:
        base_probability (float): The initial probability.
        factors (dict): A dictionary of factors with their corresponding values.

    Returns:
        float: The adjusted probability.
    """
    def adjust_weather(value):
        if value == "sunny":
            return 1.2
        elif value == "rainy":
            return 0.8
        else:
            return 1.0

    def adjust_user_input(value):
        if value == "yes":
            return 1.5
        elif value == "no":
            return 0.5
        else:
            return 1.0

    adjustment_functions = {
        "weather": adjust_weather,
        "user_input": adjust_user_input
    }

    adjusted_probability = base_probability
    for factor, value in factors.items():
        if factor in adjustment_functions:
            adjusted_probability *= adjustment_functions[factor](value)
        else:
            adjusted_probability *= 1.0

    return adjusted_probability