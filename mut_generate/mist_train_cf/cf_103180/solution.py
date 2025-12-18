"""
QUESTION:
Write a function named `counterReducer` that takes the current state and an action as input. The state is an object with a single key named "counter" and an initial value of 0. The function should handle two types of actions: 'INCREMENT' and 'DECREMENT'. When the 'INCREMENT' action is received, the function should return a new state with the counter incremented by 1. When the 'DECREMENT' action is received, the function should return a new state with the counter decremented by 1. If any other action is received, the function should return the current state unchanged.
"""

def counter_reducer(state={"counter": 0}, action=None):
    """
    This function handles two types of actions: 'INCREMENT' and 'DECREMENT'.
    It returns a new state with the counter incremented by 1 for 'INCREMENT' action,
    decremented by 1 for 'DECREMENT' action, and the current state unchanged for any other action.

    Args:
    state (dict): The current state with a single key named "counter".
    action (str): The action type. It can be 'INCREMENT', 'DECREMENT', or any other action.

    Returns:
    dict: The new state after handling the action.
    """
    if action == 'INCREMENT':
        return {"counter": state["counter"] + 1}
    elif action == 'DECREMENT':
        return {"counter": state["counter"] - 1}
    else:
        return state