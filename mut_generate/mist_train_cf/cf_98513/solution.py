"""
QUESTION:
Create a function called `adjust_air_quality(reading)` that takes an integer reading between 0 and 10 and returns the adjusted reading based on the following rules: 

- Subtract 2 if the reading is above 7.
- Add 1 if the reading is between 4 and 6 (inclusive).
- Return the original reading if it's below 4.
- Return 7 if the reading is exactly 10.
"""

def adjust_air_quality(reading):
    if reading > 7:
        return reading - 2
    elif 4 <= reading <= 6:
        return reading + 1
    elif reading < 4:
        return reading
    elif reading == 10:
        return 7