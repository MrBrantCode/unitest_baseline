"""
QUESTION:
Implement the function `calculate_rewards` that takes the following inputs: 
- `continue_value`: A 2D numpy array representing the continue values for each path at each time step.
- `immediate_reward`: A 1D numpy array representing the immediate rewards at each time step.
- `pol_sim_paths_rewards`: A 2D numpy array representing the rewards for each path at each time step.
- `discount`: A float representing the discount factor.
- `num_stages`: An integer representing the total number of stages.
- `pol_sim_sample_paths`: An integer representing the total number of sample paths.

The function should iterate through each time step, identify the paths that should be stopped based on the comparison of `continue_value` and `immediate_reward`, calculate the rewards for the stopped paths, and return the total rewards obtained from the simulation.
"""

import numpy as np

def calculate_rewards(continue_value, immediate_reward, pol_sim_paths_rewards, discount, num_stages, pol_sim_sample_paths):
    eliminated_paths = []
    reward = []
    for t in range(num_stages):
        stopping_time = np.less_equal(continue_value[:, t], immediate_reward[t])
        path_to_stop = np.setdiff1d(np.nonzero(stopping_time)[0], eliminated_paths)
        if len(path_to_stop) > 0:
            reward.extend([pol_sim_paths_rewards[_, t] * (discount ** t) for _ in path_to_stop])
            eliminated_paths.extend(path_to_stop)
    last_stage_stop = np.setdiff1d(range(pol_sim_sample_paths), eliminated_paths)
    T = num_stages
    reward.extend([pol_sim_paths_rewards[_, T - 1] * (discount ** (T - 1)) for _ in last_stage_stop])
    return sum(reward)