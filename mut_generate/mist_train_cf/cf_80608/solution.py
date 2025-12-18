"""
QUESTION:
Design a function that interprets and executes gesture commands for a Smart TV Android launcher application, assuming the existence of a machine vision system and holographic projection hardware. The function should map recognized gestures to specific commands in the Android interface.
"""

def execute_gesture_command(gesture):
    """
    Maps recognized gestures to specific commands in the Android interface.

    Args:
        gesture (str): The recognized gesture.

    Returns:
        str: The command to be executed.
    """
    gesture_commands = {
        "swipe_up": "change_channel",
        "swipe_down": "decrease_volume",
        "swipe_left": "previous_channel",
        "swipe_right": "next_channel",
        "tap": "play_pause"
    }

    return gesture_commands.get(gesture, "Invalid gesture")