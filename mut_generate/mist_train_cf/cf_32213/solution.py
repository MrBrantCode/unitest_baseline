"""
QUESTION:
Implement a function `process_switches(switches)` that takes a list of strings representing switch configurations. Return a list of integers representing the lengths of the switch configurations and a list of strings representing the stripped first elements of the switch configurations. The first element of each switch configuration string is a sequence of characters representing a specific model of the switch. The function should not modify the original switch configurations.
"""

from typing import List, Tuple

def process_switches(switches: List[str]) -> Tuple[List[int], List[str]]:
    lengths = [len(switch) for switch in switches]
    stripped_first_elements = [switch.split()[0].strip() for switch in switches]
    return (lengths, stripped_first_elements)