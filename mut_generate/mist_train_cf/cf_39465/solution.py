"""
QUESTION:
Implement the `compute_total_cost` function, which takes a system object and three lists `x`, `u`, and `t` as input and returns the total cost. The system object contains the properties `stage_cost_fn`, `terminal_cost`, and `terminal_cost_fn`, where `stage_cost_fn` computes the stage cost for a given time step, `terminal_cost` is a boolean indicating whether a terminal cost function is provided, and `terminal_cost_fn` computes the terminal cost if `terminal_cost` is True. The function should iterate through the time steps, computing the stage cost for each step and adding it to the total cost, and if a terminal cost function is provided, add the terminal cost to the total cost.
"""

def compute_total_cost(system, x, u, t):
    cost = 0
    for i in range(len(t) - 1):
        cost += system.stage_cost_fn(x[i], u[i], t[i], x[i+1], u[i+1], t[i+1])
    if system.terminal_cost:
        cost += system.terminal_cost_fn(x[-1], u[-1])
    return cost