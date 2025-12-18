"""
QUESTION:
Implement the function `update_infection_probabilities(duration, cur_succ_indices, cur_infc_indices, v_state, v_group, v_behavior)` that takes a float `duration` and lists `cur_succ_indices`, `cur_infc_indices`, `v_state`, `v_group`, and `v_behavior` as parameters, where `duration` is greater than 0.0 and the indices in `cur_succ_indices` and `cur_infc_indices` are valid indices within `v_state`, `v_group`, and `v_behavior`. The function should calculate and return the updated infection probabilities based on the given parameters.
"""

def update_infection_probabilities(duration, cur_succ_indices, cur_infc_indices, v_state, v_group, v_behavior):
    def calculate_updated_probability(ss, sg, sb, duration):
        updated_probability = ss * sg * sb * duration
        return updated_probability

    updated_probabilities = [calculate_updated_probability(v_state[i_succ], v_group[i_succ], v_behavior[i_succ], duration) for i_succ in cur_succ_indices]
    return updated_probabilities