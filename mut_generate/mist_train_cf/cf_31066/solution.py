"""
QUESTION:
Implement a function `calculate_total_resistance` that calculates the total resistance of a given electrical circuit represented as a list of components. The circuit components are either resistance values or sub-circuits enclosed within opening and closing characters. The resistance value of a sub-circuit is the sum of its components' resistance values.

The function takes two inputs: 
- `ohms`, a dictionary mapping component names to their resistance values
- `circuit`, a list of strings representing the circuit components

The function should return the total resistance of the circuit as an integer.

Assume the circuit components form a valid circuit with balanced opening and closing characters and the resistance values in `ohms` are unique for each component name.
"""

from typing import List, Dict

def calculate_total_resistance(ohms: Dict[str, int], circuit: List[str]) -> int:
    OPENING_CHARACTERS = ['(']
    CLOSING_CHARACTERS = [')']
    stack = []
    for component in circuit:
        if component in ohms:
            stack.append(ohms[component])
        elif component in OPENING_CHARACTERS:
            stack.append(component)
        elif component in CLOSING_CHARACTERS:
            sub_circuit_resistance = 0
            while stack[-1] not in OPENING_CHARACTERS:
                sub_circuit_resistance += stack.pop()
            stack.pop()  # Remove the opening character
            stack.append(sub_circuit_resistance)
        elif component == '+':
            continue  # Ignore the '+' operator
    return sum(stack)