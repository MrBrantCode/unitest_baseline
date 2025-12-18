"""
QUESTION:
Implement a class `CondDist` that represents a conditional distribution. The class should have an initializer `__init__(self, joint_dist, given_var)` that takes a joint distribution `joint_dist` and a variable `given_var` to condition on. The `joint_dist` is a dictionary where keys are tuples of joint values and values are corresponding probabilities. The `given_var` is the variable on which the distribution is conditioned.

The class should also have a method `get_distribution(self, given_value)` that returns the conditional distribution given the value of `given_var`. The method should compute the conditional distribution by summing probabilities for the given value and then normalizing the probabilities.

Additionally, implement a function `get_marginalDist(conditional_dist)` that calculates the marginal distribution from the conditional distribution.
"""

class CondDist:
    def entance(self, joint_dist, given_var):
        self.joint_dist = joint_dist
        self.given_var = given_var

    def get_distribution(self, given_value):
        conditional_dist = {}
        total_prob = 0
        for key, prob in self.joint_dist.items():
            if key[self.given_var] == given_value:
                conditional_key = key[1 - self.given_var]
                conditional_dist[conditional_key] = conditional_dist.get(conditional_key, 0) + prob
                total_prob += prob
        for key in conditional_dist:
            conditional_dist[key] /= total_prob
        return conditional_dist

def get_marginalDist(conditional_dist):
    marginal_dist = {}
    for key, prob in conditional_dist.items():
        marginal_dist[key] = marginal_dist.get(key, 0) + prob
    return marginal_dist