"""
QUESTION:
Create a function named `total_legs_on_boats` to calculate the total number of human legs on three distinct boats. The function should take no arguments but use the following variables for each boat: `boat1_pirates`, `boat1_sailors`, `boat2_pirates`, `boat2_sailors`, `boat3_pirates`, and `boat3_sailors`. The function should return the total number of legs on each boat and the grand total of legs across all boats.
"""

def total_legs_on_boats(boat1_pirates, boat1_sailors, boat2_pirates, boat2_sailors, boat3_pirates, boat3_sailors):
    # total number of legs on each boat
    boat1_legs = (boat1_pirates + boat1_sailors) * 2
    boat2_legs = (boat2_pirates + boat2_sailors) * 2
    boat3_legs = (boat3_pirates + boat3_sailors) * 2

    # grand total number of legs
    total_legs = boat1_legs + boat2_legs + boat3_legs

    return boat1_legs, boat2_legs, boat3_legs, total_legs