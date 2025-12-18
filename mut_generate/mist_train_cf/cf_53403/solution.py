"""
QUESTION:
Implement a function that models a Partially Observable Markov Decision Process (POMDP) where the next state depends on the current action, the current state, and an external input (observation).
"""

def pomdp_transition(current_state, action, observation):
    """
    Models a Partially Observable Markov Decision Process (POMDP) where the next state depends on the current action, the current state, and an external input (observation).

    Parameters:
    current_state (str): The current state of the system.
    action (str): The action taken by the agent.
    observation (str): The external input or observation.

    Returns:
    next_state (str): The next state of the system.
    """
    # This is a very simplified example and real-world scenarios would require a more complex implementation
    # For the sake of simplicity, let's assume we have a dictionary that maps the current state, action, and observation to the next state
    transitions = {
        ('state1', 'action1', 'observation1'): 'state2',
        ('state1', 'action2', 'observation2'): 'state3',
        # Add more transitions here...
    }

    return transitions.get((current_state, action, observation), 'unknown_state')