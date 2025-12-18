"""
QUESTION:
You are given two numpy arrays, `production` and `costs`. The `production` array has three fields: "name", "production_cond1", and "production_cond2", representing the name of each gene and its production levels under two different temperature conditions. The `costs` array has two fields: "name" and "cost", representing the name of each gene and its associated induction cost.

Write a function `most_cost_effective_gene(production, costs)` that returns a dictionary with keys "Temperature1" and "Temperature2". The values for each key should be a tuple containing the name of the most cost-effective gene and its associated cost for each temperature condition. If multiple genes have the same lowest cost, the one with the lowest production should be chosen.
"""

import numpy as np

def most_cost_effective_gene(production, costs):
    # Calculate the total cost for each gene under each temperature condition
    total_cost_cond1 = production["production_cond1"] * costs["cost"]
    total_cost_cond2 = production["production_cond2"] * costs["cost"]

    # Find the index of the gene with the lowest total cost for each temperature condition
    min_cost_index_cond1 = np.argmin(total_cost_cond1)
    min_cost_index_cond2 = np.argmin(total_cost_cond2)

    # Get the name and cost of the most cost-effective gene for each temperature condition
    most_cost_effective_cond1 = (production["name"][min_cost_index_cond1], total_cost_cond1[min_cost_index_cond1])
    most_cost_effective_cond2 = (production["name"][min_cost_index_cond2], total_cost_cond2[min_cost_index_cond2])

    return {"Temperature1": most_cost_effective_cond1, "Temperature2": most_cost_effective_cond2}