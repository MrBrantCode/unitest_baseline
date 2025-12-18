"""
QUESTION:
Implement the `get_advantages` method, which takes four parameters: `observations`, `actions`, `rewards`, and `terminals`, and calculates the advantages for each state-action pair based on the observed rewards and estimated state values. The `observations` is a list of observed states, `actions` is a list of actions taken in each state, `rewards` is a list of rewards received after taking each action, and `terminals` is a list indicating whether each state is a terminal state (True) or not (False). The advantages are calculated using the formula `advantage = Q(s, a) - V(s)`, where `Q(s, a)` is the estimated value of taking action `a` in state `s`, and `V(s)` is the estimated value of being in state `s`. If the state is a terminal state, the advantage is simply the reward.
"""

def get_advantages(observations, actions, rewards, terminals, critic):
    advantages = []
    for i in range(len(observations)):
        if terminals[i]:  
            advantages.append(rewards[i])
        else:
            state_value = critic.estimate_state_value(observations[i])
            action_value = critic.estimate_action_value(observations[i], actions[i])
            advantage = action_value - state_value
            advantages.append(advantage)
    return advantages