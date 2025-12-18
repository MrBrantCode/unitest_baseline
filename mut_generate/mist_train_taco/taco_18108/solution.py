"""
QUESTION:
Good job! Now that Heidi is able to distinguish between Poisson and uniform distributions, she is in a good position to actually estimate the populations.

Can you help Heidi estimate each village's population?


-----Input-----

Same as the easy version.


-----Output-----

Output one line per village, in the same order as provided in the input, containing your (integer) population estimate.

Your answer is considered correct if it is an integer that falls into the interval $[ \lfloor 0.95 \cdot P \rfloor, \lceil 1.05 \cdot P \rceil ]$, where P is the real population of the village, used to create the distribution (either Poisson or uniform) from which the marmots drew their answers.
"""

def estimate_village_populations(village_estimates):
    """
    Estimate the population of each village based on the given estimates.

    Parameters:
    village_estimates (list of lists): A list where each element is a list of population estimates for a village.

    Returns:
    list of int: A list of population estimates for each village.
    """
    def sample_variance(V):
        X = sum(V) / len(V)
        S = 0.0
        for x in V:
            S += (X - x) ** 2
        S /= len(V) - 1
        return (X, S)

    population_estimates = []
    for V in village_estimates:
        (X, S) = sample_variance(V)
        v1 = X
        v2 = (2 * X) ** 2 / 12
        if abs(v1 - S) < abs(v2 - S):
            population_estimates.append(int(X))
        else:
            population_estimates.append(max(V) + min(V) // 2)
    
    return population_estimates