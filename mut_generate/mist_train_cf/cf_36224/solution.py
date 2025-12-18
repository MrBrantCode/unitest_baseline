"""
QUESTION:
Write a function `parse_quantum_circuit(code: str) -> List[str]` that takes a string `code` representing a quantum circuit manipulation code snippet and returns a list of strings representing the sequence of operations performed on the quantum circuit. The code snippet consists of operations performed on a quantum circuit using a handler, where each operation is represented by a line of code. The function should extract the operations performed on the quantum circuit from the given code snippet and return them as a list of strings, ignoring empty lines and comments.
"""

from typing import List

def parse_quantum_circuit(code: str) -> List[str]:
    operations = []
    lines = code.split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            operations.append(line)
    return operations