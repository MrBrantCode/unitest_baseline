"""
QUESTION:
Write a function `displayThermometer` that takes two parameters: `currentTemp` (integer) and `maxTemp` (integer). The function should return a string representing the visual display of a thermometer bar within a defined range, where the color of the bar changes based on the temperature level: blue (0°C - 10°C), green (11°C - 20°C), yellow (21°C - 30°C), orange (31°C - 35°C), and red (36°C - maxTemp).
"""

def displayThermometer(currentTemp, maxTemp):
    temperature_level = (currentTemp / maxTemp) * 100

    if currentTemp <= 10:
        color = "blue"
    elif currentTemp <= 20:
        color = "green"
    elif currentTemp <= 30:
        color = "yellow"
    elif currentTemp <= 35:
        color = "orange"
    else:
        color = "red"

    filled_length = int(temperature_level * 0.5)
    display_bar = f'<div class="thermometer-div" style="border: 2px solid #03f; height: 1em; width: 50%;"><div style="background-color: {color}; width: {filled_length}%; height: 100%;"></div></div>'
    
    return display_bar