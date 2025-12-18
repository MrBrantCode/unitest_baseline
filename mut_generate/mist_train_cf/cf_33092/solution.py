"""
QUESTION:
Implement a function `filter_modules` that takes in a list of module objects and a layer name as input and returns a list of footprints for modules that meet the following criteria:
1. The module's layer matches the given layer name.
2. The x-coordinate of the module's position is greater than 0.

Each module object contains information about the component's position, orientation, description, layer, and footprint, and has the following attributes:
- `position`: A tuple (x, y, z) representing the position of the module.
- `layer`: The layer of the module.
- `footprint`: The name of the footprint library item.

The function signature is `def filter_modules(modules: List[Module], layer_name: str) -> List[str]:`
"""

from typing import List

class Module:
    def __init__(self, position, orientation, description, layer, footprint):
        self.position = position
        self.orientation = orientation
        self.description = description
        self.layer = layer
        self.footprint = footprint

def filter_modules(modules: List[Module], layer_name: str) -> List[str]:
    return [mod.footprint for mod in modules if mod.layer == int(layer_name) and mod.position[0] > 0]