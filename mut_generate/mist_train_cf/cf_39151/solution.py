"""
QUESTION:
Implement a `state` method for a `StateMachine` class that takes an input `action` and returns a tuple `(goto_next, new_state)`. The `state` method should transition between states based on the input `action` and the current `state_action_type`. The `goto_next` value indicates whether to move to the next column in the algorithm, and `new_state` is the next state after processing the input `action`. The class should have a `state_action_type` attribute and a `column` attribute initialized to 0. The `state_action_type` can be 1, 2, or 3, and the `action` can also be 1, 2, or 3.
"""

def state(state_action_type, action):
    """
    Transition between states based on the input action and the current state_action_type.

    Args:
        state_action_type (int): The current state action type (1, 2, or 3).
        action (int): The input action (1, 2, or 3).

    Returns:
        tuple: A tuple containing two values: 
            - goto_next (bool): Whether to move to the next column.
            - new_state (int): The next state after processing the input action.
    """
    if state_action_type == 1:
        if action == 1:
            return (True, 2)
        elif action == 2:
            return (True, 3)
        elif action == 3:
            return (True, 1)
    elif state_action_type == 2:
        if action == 1:
            return (True, 3)
        elif action == 2:
            return (True, 1)
        elif action == 3:
            return (True, 2)
    elif state_action_type == 3:
        if action == 1:
            return (True, 1)
        elif action == 2:
            return (True, 2)
        elif action == 3:
            return (True, 3)
    return (False, state_action_type)