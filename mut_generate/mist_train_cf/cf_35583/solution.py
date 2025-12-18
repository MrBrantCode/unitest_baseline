"""
QUESTION:
Write a function `volume_control` that takes in an initial volume level, a list of button clicks, and a dictionary of configuration parameters for "button_down", "button_up", and "button_mute". The function should return the final volume level after processing all the button clicks, considering the following rules:

- Each button click is either "down", "up", or "mute".
- If a button is not disabled (i.e., its configuration value is not 0), the volume should be adjusted accordingly.
- The volume should not go below 0 when "button_down" is pressed, and should not exceed 100 when "button_up" is pressed.
- The "mute" button toggles the volume between 0 and 100, unless the volume is already at 0, in which case it sets it to 100.

The function signature is:
```python
def volume_control(initial_volume: int, button_clicks: List[str], button_config: Dict[str, int]) -> int
```
Assume that the initial volume is within the range of 0 to 100 (inclusive).
"""

from typing import List, Dict

def volume_control(initial_volume: int, button_clicks: List[str], button_config: Dict[str, int]) -> int:
    volume = initial_volume
    for click in button_clicks:
        if click == "down" and button_config["button_down"] != 0:
            volume = max(0, volume - button_config["button_down"])
        elif click == "up" and button_config["button_up"] != 0:
            volume = min(100, volume + button_config["button_up"])
        elif click == "mute" and button_config["button_mute"] != 0:
            volume = 0 if volume != 0 else 100  
    return volume