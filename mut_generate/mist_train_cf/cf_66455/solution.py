"""
QUESTION:
Define a function volumeIncrease() that takes three parameters: initial length, width, and height of a rectangular prism. The function should calculate the cumulative volume increase of the prism over a specified period, where the dimensions increase as follows: length by 2cm per day over 3 days, width by 3cm per day over 5 days, and height by 1cm per day over 4 days.
"""

def volume_increase(length, width, height):
    initial_volume = length * width * height
    for _ in range(3):
        length += 2
    for _ in range(5):
        width += 3
    for _ in range(4):
        height += 1
    final_volume = length * width * height
    volume_increase = final_volume - initial_volume
    return volume_increase