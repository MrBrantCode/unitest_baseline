"""
QUESTION:
Create a function `average_of_the_best` that takes a dictionary `results` and a string `reward_key` as input. The `results` dictionary has scheme names as keys and dictionaries containing the scheme's results as values. Each scheme's results dictionary contains a key `reward_key` with a list of rewards. The function should return the average reward of the best-performing scheme.
"""

import numpy as np

def average_of_the_best(results: dict, reward_key: str) -> float:
    avg_best = -1000000000000
    for scheme in results.keys():
        avg_tmp = np.mean(results[scheme][reward_key])
        if avg_best < avg_tmp:
            avg_best = avg_tmp
    return avg_best