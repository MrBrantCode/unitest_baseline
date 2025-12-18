"""
QUESTION:
Implement the `count_solutions` function to calculate the number of possible solutions to reach a target score by adding or subtracting a fixed set of scores. The function should take an `initial_score` and a `target_score` as input, assuming both are non-negative integers, and a fixed set of scores as a non-empty set of positive integers.
"""

def count_solutions(initial_score, target_score, fixed_set_of_scores):
    if target_score == 0:
        return 1  
    if initial_score > target_score:
        return 0  

    solutions = [0] * (target_score + 1)
    solutions[0] = 1  

    for score in range(1, target_score + 1):
        for fixed_score in fixed_set_of_scores:
            if score - fixed_score >= 0:
                solutions[score] += solutions[score - fixed_score]

    return solutions[target_score]