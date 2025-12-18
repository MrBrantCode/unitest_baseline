"""
QUESTION:
Implement the `crossover` and `biasCrossover` functions, which take two lists of numbers (weights or biases) of equal length and perform crossover at the midpoint to produce two offspring lists. The crossover operation should combine the first half of the first list with the second half of the second list, and vice versa. The functions should return a list containing the two offspring lists.
"""

def crossover(parent1, parent2):
    """
    This function performs crossover at the midpoint of two lists of numbers to produce two offspring lists.

    Args:
    parent1 (list): The first list of numbers.
    parent2 (list): The second list of numbers.

    Returns:
    list: A list containing the two offspring lists.
    """
    crossover_point = len(parent1) // 2  
    children = [parent1[:crossover_point] + parent2[crossover_point:], 
                parent2[:crossover_point] + parent1[crossover_point:]]  
    return children

def biasCrossover(parent1, parent2):
    """
    This function performs crossover at the midpoint of two lists of numbers to produce two offspring lists.

    Args:
    parent1 (list): The first list of numbers.
    parent2 (list): The second list of numbers.

    Returns:
    list: A list containing the two offspring lists.
    """
    crossover_point = len(parent1) // 2  
    children = [parent1[:crossover_point] + parent2[crossover_point:], 
                parent2[:crossover_point] + parent1[crossover_point:]]  
    return children