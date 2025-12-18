"""
QUESTION:
Create a function `optimize_quantum_cost` that takes a dictionary `cut_solution` as input, where `cut_solution` contains the keys 'counter', 'classical_cost', 'quantum_cost', and 'quantum_cost_weight'. The function should calculate the optimized quantum cost by multiplying the original quantum cost with the quantum cost weight and update the 'quantum_cost' value in the dictionary. It should also calculate the optimized classical cost by subtracting the optimized quantum cost from the classical cost and update the 'classical_cost' value in the dictionary. Additionally, the function should print the model's objective value, MIP runtime, and whether the optimization is optimal or not. The function should return the modified `cut_solution` dictionary with the updated quantum and classical costs. The input dictionary and the model's objective value, MIP runtime, and optimality status are assumed to be available. 

The function should have the following signature: `def optimize_quantum_cost(cut_solution: dict) -> dict`.
"""

def optimize_quantum_cost(cut_solution: dict, best_mip_model: object) -> dict:
    quantum_cost_weight = cut_solution['quantum_cost_weight']
    optimized_quantum_cost = cut_solution['quantum_cost'] * quantum_cost_weight
    optimized_classical_cost = cut_solution['classical_cost'] - optimized_quantum_cost

    print('Model objective value = %.2e' % (best_mip_model.objective), flush=True)
    print('MIP runtime:', best_mip_model.runtime, flush=True)

    if best_mip_model.optimal:
        print('OPTIMAL, MIP gap =', best_mip_model.mip_gap, flush=True)
    else:
        print('NOT OPTIMAL, MIP gap =', best_mip_model.mip_gap, flush=True)
    print('-' * 20, flush=True)

    cut_solution['quantum_cost'] = optimized_quantum_cost
    cut_solution['classical_cost'] = optimized_classical_cost
    return cut_solution