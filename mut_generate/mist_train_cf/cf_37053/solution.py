"""
QUESTION:
Implement the function `calculate_objective_value(circuit, preparation_circuit, ansatz, result, objective)` that takes a quantum circuit, preparation circuit, ansatz object, the final wavefunction obtained from the circuit, and an objective object as input. The function should return the calculated objective value based on the given result.

Restrictions: 
- The function should use the given objective object to calculate the objective value.
- The objective object should have a method `value(result)` that calculates the objective value based on the given result.
- The function should not modify the input parameters.
"""

def calculate_objective_value(circuit, preparation_circuit, ansatz, result, objective):
    """
    Calculate the objective value based on the given result.

    Args:
        circuit: A quantum circuit.
        preparation_circuit: A preparation circuit.
        ansatz: An ansatz object.
        result: The final wavefunction obtained from the circuit.
        objective: An objective object with a method 'value(result)'.

    Returns:
        The calculated objective value.
    """
    obj_val = objective.value(result)
    return obj_val