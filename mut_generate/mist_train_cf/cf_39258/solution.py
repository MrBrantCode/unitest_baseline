"""
QUESTION:
Implement the function `update_arrays(state, action_index, reward, weights, flags, glows, n, gamma, memory)` that updates the weights, flags, and glows arrays based on the given conditions and returns the updated memory dictionary. The function takes in the following parameters: `state`, `action_index`, `reward`, `weights`, `flags`, `glows`, `n`, `gamma`, and `memory`. It should update the arrays as follows:

- Update the glows array by setting the element at the action index to 1.0 and all other elements to (1 - n) * g, where n is the given parameter and g is the original value at that index.
- Update the weights array at the action index using the formula: weights[action_index] = weights[action_index] - gamma * (weights[action_index] - 1) + glows[action_index] * reward, where gamma is a predefined constant.
- If the reward is less than 0.0, remove the element at the action index from the flags array. If the flags array becomes empty after this removal, reinitialize it with indices excluding the action index.
- Update the memory dictionary with the new values of weights, flags, and glows for the given state.

Assume that the input arrays (weights, flags, glows) are NumPy arrays of the same length. The memory dictionary has the state as the key and a tuple of (weights, flags, glows) as the value.
"""

import numpy as np

def update_arrays(state, action_index, reward, weights, flags, glows, n, gamma, memory) -> dict:
    updated_glows = np.array([1.0 if i == action_index else (1 - n) * g for i, g in enumerate(glows)])

    updated_weights = weights.copy()
    updated_weights[action_index] = updated_weights[action_index] - gamma * (updated_weights[action_index] - 1) + updated_glows[action_index] * reward

    updated_flags = np.delete(flags, action_index) if reward < 0.0 else flags
    if len(updated_flags) == 0:
        updated_flags = np.array([i for i in range(len(weights)) if i != action_index])

    memory[state] = (updated_weights, updated_flags, updated_glows)

    return memory