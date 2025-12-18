"""
QUESTION:
Your task is the exact same as for the easy version. But this time, the marmots subtract the village's population P from their random number before responding to Heidi's request.

Also, there are now villages with as few as a single inhabitant, meaning that $1 \leq P \leq 1000$.

Can you help Heidi find out whether a village follows a Poisson or a uniform distribution?


-----Input-----

Same as for the easy and medium versions. But remember that now 1 ≤ P ≤ 1000 and that the marmots may provide positive as well as negative integers.


-----Output-----

Output one line per village, in the same order as provided in the input. The village's line shall state poisson if the village's distribution is of the Poisson type, and uniform if the answers came from a uniform distribution.
"""

def determine_distribution(village_responses):
    """
    Determines whether the distribution of responses from a village is Poisson or Uniform.

    Parameters:
    village_responses (list of int): A list of integers representing the responses from the marmots.

    Returns:
    str: A string indicating the type of distribution, either "poisson" or "uniform".
    """
    def sample_variance(V):
        X = sum(V) / len(V)
        S = 0.0
        for x in V:
            S += (X - x) ** 2
        S /= len(V) - 1
        return (X, S)
    
    (X, S) = sample_variance(village_responses)
    return 'uniform' if max(village_responses) < 1.9 * S ** 0.5 else 'poisson'