"""
QUESTION:
Write a function in Python that replicates the functionality of the `data-confirm` attribute in Rails, which generates a JavaScript `confirm` call. This function should prompt the user with a specified message and return `True` if the user confirms and `False` otherwise.

The function should be named `confirm_dialog` and it should take a single argument `message`. The function should not rely on any external libraries or frameworks.
"""

def confirm_dialog(message):
    """
    This function replicates the functionality of the `data-confirm` attribute in Rails.
    It prompts the user with a specified message and returns `True` if the user confirms and `False` otherwise.

    Args:
        message (str): The message to be displayed in the confirmation dialog.

    Returns:
        bool: `True` if the user confirms, `False` otherwise.
    """
    return input(f"{message} (yes/no): ").lower() == "yes"