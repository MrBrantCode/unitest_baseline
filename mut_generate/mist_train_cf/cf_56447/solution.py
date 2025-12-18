"""
QUESTION:
Create a function named `simsons_paradox_example` that demonstrates a real-world example of Simpson's paradox, where a positive correlation within individual groups reverses when the groups are combined. The function should illustrate this phenomenon using a simple example, such as a medical research study with two cities, and account for the effects of a confounding variable.
"""

def simsons_paradox_example(city_a_treatment, city_a_recovery, city_b_treatment, city_b_recovery):
    """
    Demonstrates Simpson's paradox using a simple medical research example.

    Args:
        city_a_treatment (list): Treatment rates in City A.
        city_a_recovery (list): Recovery rates in City A.
        city_b_treatment (list): Treatment rates in City B.
        city_b_recovery (list): Recovery rates in City B.

    Returns:
        tuple: Correlation between treatment and recovery in City A, City B, and combined.
    """

    # Calculate correlation within each city
    corr_city_a = sum(x * y for x, y in zip(city_a_treatment, city_a_recovery)) / (sum(x * x for x in city_a_treatment) * sum(y * y for y in city_a_recovery)) ** 0.5
    corr_city_b = sum(x * y for x, y in zip(city_b_treatment, city_b_recovery)) / (sum(x * x for x in city_b_treatment) * sum(y * y for y in city_b_recovery)) ** 0.5

    # Calculate combined correlation
    combined_treatment = [x for x in city_a_treatment] + [x for x in city_b_treatment]
    combined_recovery = [y for y in city_a_recovery] + [y for y in city_b_recovery]
    corr_combined = sum(x * y for x, y in zip(combined_treatment, combined_recovery)) / (sum(x * x for x in combined_treatment) * sum(y * y for y in combined_recovery)) ** 0.5

    return corr_city_a, corr_city_b, corr_combined