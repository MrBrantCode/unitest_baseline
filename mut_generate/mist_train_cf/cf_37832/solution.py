"""
QUESTION:
Implement a function `write_to_pipette_memory` that simulates writing a pipette's unique identifier and model to its memory. The function takes three parameters: `mount`, `identifier`, and `model`. The `mount` parameter is a string that can be either "left" or "right", representing the location of the pipette. The `identifier` and `model` parameters are non-empty strings representing the unique identifier and model of the pipette, respectively.

The function should write the `identifier` and `model` to the memory of the specified pipette and return a message indicating the success of the operation. Note that the `mount`, `identifier`, and `model` parameters will always adhere to the specified constraints.
"""

from typing import Union

class Pipette:
    def __init__(self, mount: str):
        self.mount = mount
        self.identifier = None
        self.model = None

def write_to_pipette_memory(mount: str, identifier: str, model: str) -> str:
    pipette = Pipette(mount)
    pipette.identifier = identifier
    pipette.model = model
    return f"Successfully wrote identifier '{identifier}' and model '{model}' to the memory of the {mount} pipette."