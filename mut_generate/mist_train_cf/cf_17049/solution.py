"""
QUESTION:
Create a function named `convert_to_rainbow_color` that takes a string input and returns its corresponding enumerated type from the colors of the rainbow ("Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"). The enumerated type should be implemented using a custom-defined class, not the built-in enum type. If the input string does not match any of the colors, the function should return `None`.
"""

class RainbowColor:
    def __init__(self, name):
        self.name = name

# Define the colors of the rainbow
red = RainbowColor("Red")
orange = RainbowColor("Orange")
yellow = RainbowColor("Yellow")
green = RainbowColor("Green")
blue = RainbowColor("Blue")
indigo = RainbowColor("Indigo")
violet = RainbowColor("Violet")

def convert_to_rainbow_color(color_string):
    color_string = color_string.lower()
    switch = {
        "red": red,
        "orange": orange,
        "yellow": yellow,
        "green": green,
        "blue": blue,
        "indigo": indigo,
        "violet": violet
    }
    return switch.get(color_string, None)