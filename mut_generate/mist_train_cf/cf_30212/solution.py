"""
QUESTION:
Implement the `rename_signal` function, which takes three parameters: the original signal name (`original_signal`), the renaming condition (`renaming_condition`), and the new name for the renamed signal (`new_name`). The function should return a string representing the renamed signal, which includes the new name and the renaming condition. The renaming condition can contain logical operations (AND `&`, OR `|`, NOT `~`) and signal references.
"""

def rename_signal(original_signal, renaming_condition, new_name):
    # Apply the renaming condition to the original signal
    renamed_signal = f"{new_name} = {renaming_condition}"
    
    return renamed_signal