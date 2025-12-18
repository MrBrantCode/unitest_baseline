"""
QUESTION:
Create a function `colorizeMessage` that takes a message string, a color code, and a boolean flag to apply the color. The function should apply the specified color to the message if the flag is `True` and return the colorized message. If the flag is `False` or the color code is not found, return the original message. The color codes and their corresponding escape sequences should be stored in a color map. 

The function should accept the following parameters:
- `message` (string): The message to be colorized.
- `colorCode` (string): The code representing the color to be applied.
- `applyColor` (boolean): A flag indicating whether to apply the color to the message.

The color map should include at least the color code "LBLUE" with its corresponding escape sequence.
"""

def colorizeMessage(message, colorCode, applyColor):
    colorMap = {
        "LBLUE": "\033[94m",  # Light Blue color code
        # Add more color codes as needed
    }
    
    if applyColor and colorCode.upper() in colorMap:
        return f"{colorMap[colorCode.upper()]}{message}\033[0m"  # Apply color and reset to default
    else:
        return message