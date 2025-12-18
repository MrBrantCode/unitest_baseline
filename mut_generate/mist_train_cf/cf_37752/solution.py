"""
QUESTION:
Create a Python class `AlertsManager` that can manage presets for different categories of alerts and popups. The class should have the following methods: 

- `add_preset(category: str, description: str)`: Adds a preset description to the specified category.
- `get_presets(category: str) -> List[str]`: Returns a list of presets for the specified category.
- `get_all_presets() -> Dict[str, List[str]]`: Returns a dictionary containing all categories as keys and their respective presets as values.

Restrictions: None
"""

from typing import List, Dict

def add_preset(data_source, category: str, description: str):
    """Adds a preset description to the specified category."""
    for i, (cat, presets) in enumerate(data_source):
        if cat == category:
            data_source[i] = (cat, presets + [description])
            return
    data_source.append((category, [description]))

def get_presets(data_source, category: str) -> List[str]:
    """Returns a list of presets for the specified category."""
    for cat, presets in data_source:
        if cat == category:
            return presets
    return []

def get_all_presets(data_source) -> Dict[str, List[str]]:
    """Returns a dictionary containing all categories as keys and their respective presets as values."""
    return {cat: presets for cat, presets in data_source}