"""
QUESTION:
Create a function named `counterReducer` that takes in an object `state` with a key `counter` and an `action` object with a `type` and `payload`. The initial state should have a `counter` value of 0. The function should handle two action types: "INCREMENT" and "DECREMENT". It should update the `counter` state by adding or subtracting the `payload` value based on the action type. If the `payload` is not a finite number, the function should return the original state. The function should have a time complexity of O(1) for both "INCREMENT" and "DECREMENT" operations.
"""

def counterReducer(state={"counter": 0}, action=None):
    """
    Reduces the counter state based on the given action.

    Args:
    state (dict): The current state with a 'counter' key. Defaults to {'counter': 0}.
    action (dict): The action to perform with 'type' and 'payload' keys.

    Returns:
    dict: The updated state after applying the action.
    """
    if action is None:
        return state
    
    payload = action.get('payload')
    if not isinstance(payload, (int, float)) or not payload == payload or not abs(payload) < float('inf'):
        return state

    if action.get('type') == "INCREMENT":
        return {"counter": state['counter'] + payload}
    elif action.get('type') == "DECREMENT":
        return {"counter": state['counter'] - payload}
    else:
        return state