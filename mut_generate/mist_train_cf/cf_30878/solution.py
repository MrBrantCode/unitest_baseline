"""
QUESTION:
Implement a function `state_transition(current_state, input)` that takes the current state (0, 1, or 2) and input ("A" or "B") as parameters and returns the next state based on the following rules:
- From state 0: "A" transitions to state 1, "B" transitions to state 2.
- From state 1: "A" transitions to state 0, "B" remains in state 1.
- From state 2: "A" remains in state 2, "B" transitions to state 0.
If the input is neither "A" nor "B", the function should return the current state.
"""

def state_transition(current_state, input):
    if current_state == 0:
        if input == "A":
            return 1
        elif input == "B":
            return 2
    elif current_state == 1:
        if input == "A":
            return 0
        elif input == "B":
            return 1
    elif current_state == 2:
        if input == "A":
            return 2
        elif input == "B":
            return 0
    return current_state  # Return current state if input is invalid