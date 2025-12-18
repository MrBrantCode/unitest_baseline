"""
QUESTION:
Create a Python class `KeyBinding` with a method `perform_action` that takes a key combination as input and returns the associated action from a predefined set of key bindings. The predefined key bindings are "^A" for "beginning-of-line", "^E" for "end-of-line", "^B" for "vi-backward-word", "^F" for "vi-forward-word", "^W" for "vi-backward-kill-word", and "^[ " for "vi-cmd-mode". If the input key combination does not have an associated action, the method should return "No action found".
"""

def perform_action(key_combination):
    bindings = {
        "^A": "beginning-of-line",
        "^E": "end-of-line",
        "^B": "vi-backward-word",
        "^F": "vi-forward-word",
        "^W": "vi-backward-kill-word",
        "^[": "vi-cmd-mode"
    }
    return bindings.get(key_combination, "No action found")