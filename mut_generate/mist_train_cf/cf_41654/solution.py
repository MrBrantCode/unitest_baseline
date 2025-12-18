"""
QUESTION:
Implement a function `calculate_cost` that takes in two parameters: `predicted_states` and `reference_states`, both of which are lists of 4-dimensional state vectors. The function should return the total cost, which is defined as the sum of squared errors between the predicted state and the reference state at each time step. The error is calculated as the difference between corresponding elements of the predicted state and the reference state. The total cost should be calculated over a given time horizon, which is the length of the `predicted_states` or `reference_states` list. The function should not take any additional parameters.
"""

def calculate_cost(predicted_states, reference_states):
    """
    This function calculates the total cost as the sum of squared errors 
    between the predicted state and the reference state at each time step.

    Parameters:
    predicted_states (list): A list of 4-dimensional state vectors.
    reference_states (list): A list of 4-dimensional state vectors.

    Returns:
    float: The total cost.
    """
    total_cost = 0.0
    for k in range(len(predicted_states)):
        error = [predicted_states[k][i] - reference_states[k][i] for i in range(4)]
        total_cost += sum([e**2 for e in error])
    return total_cost