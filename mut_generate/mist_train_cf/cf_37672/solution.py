"""
QUESTION:
Create a Python module with the following components: 

- `Treant` class with an initializer that takes a `name` parameter.
- `Tree` class that inherits from `Treant`, with an initializer that takes `name` and `children` parameters (defaulting to an empty list if `children` is `None`).
- `Leaf` class that inherits from `Treant`, with an initializer that takes a `name` parameter.
- `Bundle` class with an initializer that takes a `components` parameter (defaulting to an empty list if `components` is `None`).
- `discover` function that takes a `tree` and a `component_type` as parameters and returns a list of discovered components of the given type.
- `View` class with a static method `display` that takes a list of `components` and a `format_type` parameter (defaulting to 'default') and displays the components accordingly.

Implement these components so they can be used together to create, manipulate, and view tree structures.
"""

class Treant:
    def __init__(self, name):
        self.name = name

class Tree(Treant):
    def __init__(self, name, children=None):
        super().__init__(name)
        self.children = children if children is not None else []

class Leaf(Treant):
    def __init__(self, name):
        super().__init__(name)

class Bundle:
    def __init__(self, components=None):
        self.components = components if components is not None else []

def entrance(tree, component_type):
    discovered_components = []

    def _discover_helper(node, component_type):
        if isinstance(node, component_type):
            discovered_components.append(node)
        if isinstance(node, Tree):
            for child in node.children:
                _discover_helper(child, component_type)

    _discover_helper(tree, component_type)
    return discovered_components

class View:
    @staticmethod
    def display(components, format_type='default'):
        if format_type == 'default':
            for component in components:
                print(component.name)
        # Add support for other format types as needed