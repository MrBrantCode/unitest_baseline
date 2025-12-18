"""
QUESTION:
Design two functions, `calculate_one_rep_max` and `calculate_optimal_weight_reps`, to calculate the one-rep max for a given exercise and the optimal weight and reps for a given number of sets, respectively. The one-rep max formula is `weight_lifted * (1 + (number of repetitions / 30))`. The optimal weight and reps formulas are `weight = one-rep max / (1.0278 - (0.0278 * reps))` and `reps = (one-rep max / weight + 0.0278) / 1.0278`.
"""

def one_rep_max(weight_lifted, num_reps):
    """
    Calculate the one-rep max for a given exercise.

    Parameters:
    weight_lifted (float): The weight lifted.
    num_reps (int): The number of repetitions.

    Returns:
    float: The one-rep max.
    """
    return weight_lifted * (1 + (num_reps / 30))

def optimal_weight_reps(one_rep_max, num_sets):
    """
    Calculate the optimal weight and reps for a given number of sets.

    Parameters:
    one_rep_max (float): The one-rep max.
    num_sets (int): The number of sets.

    Returns:
    tuple: A tuple containing the optimal weight and reps.
    """
    weight = one_rep_max / (1.0278 - (0.0278 * num_sets))
    reps = (one_rep_max / weight + 0.0278) / 1.0278
    return weight, reps