"""
QUESTION:
Write a function `is_entangled` that determines if two particles are entangled based on their state. The particles' states are represented as strings of '0's and '1's, and they are entangled if and only if the first particle's state is the opposite of the second particle's state when XORed with a control string. The control string is also a string of '0's and '1's.
"""

def is_entangled(state1, state2, control):
    return state1 != control and state2 != control and state1 != state2