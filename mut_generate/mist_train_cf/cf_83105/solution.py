"""
QUESTION:
Design a function to emulate a T flip-flop circuit in Python. The function should take an input 't' and return the output of the flip-flop after toggling its state if 't' is 1. If 't' is 0, the state remains the same. The initial state of the flip-flop is 0.
"""

def t_flip_flop(t, previous_state=0):
    if t == 1:
        return 1 if previous_state == 0 else 0
    else:
        return previous_state