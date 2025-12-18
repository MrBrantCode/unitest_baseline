"""
QUESTION:
Create a function `calculate_one_rep_max` that calculates the one-rep max for a given exercise using the formula `weight lifted * (1 + (number of repetitions / 30))`. The function should take `weight_lifted` and `num_reps` as input and return the calculated one-rep max. 

Also, create a function `calculate_optimal_weight_reps` that calculates the optimal weight and reps for a given number of sets using the formulas `weight = one-rep max / (1.0278 - (0.0278 * reps))` and `reps = (one-rep max / weight + 0.0278) / 1.0278`. The function should take `one_rep_max` and `num_sets` as input and return the calculated weight and reps.
"""

def calculate_one_rep_max(weight_lifted, num_reps):
    one_rep_max = weight_lifted * (1 + (num_reps / 30))
    return one_rep_max

def calculate_optimal_weight_reps(one_rep_max, num_sets):
    weight = one_rep_max / (1.0278 - (0.0278 * num_sets))
    reps = (one_rep_max / weight + 0.0278) / 1.0278
    return weight, reps