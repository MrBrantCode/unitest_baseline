"""
QUESTION:
Implement the `calculate_joint_probability_distribution` function to construct the joint probability distribution based on the given data. The function should take the following parameters: `Y_dev`, a list of lists containing data points for the random variables; `Ys_ordered`, an ordered list of random variables; and `cardinalities`, a list of cardinalities of the random variables. The function should return a `JointProbabilityDistribution` object representing the joint probability distribution of the given random variables. The `JointProbabilityDistribution` class is defined as having an `__init__` method that takes `variables`, `cardinalities`, and `probabilities` as parameters.
"""

from collections import defaultdict
import itertools

def calculate_joint_probability_distribution(Y_dev, Ys_ordered, cardinalities):
    counts = defaultdict(int)
    for data_point in Y_dev:
        counts[tuple(data_point)] += 1

    Y_vecs = list(itertools.product(*[range(card) for card in cardinalities]))
    probabilities = [
        float(counts[tuple(Y_vec)]) / len(Y_dev)
        for Y_vec in Y_vecs
    ]

    class JointProbabilityDistribution:
        def __init__(self, variables, cardinalities, probabilities):
            self.variables = variables
            self.cardinalities = cardinalities
            self.probabilities = probabilities

    return JointProbabilityDistribution(Ys_ordered, cardinalities, probabilities)