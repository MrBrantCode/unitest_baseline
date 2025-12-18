"""
QUESTION:
Create a function called `convert_pressure` that takes three parameters: `from_unit`, `to_unit`, and `value`. The `from_unit` and `to_unit` parameters should be one of the following strings: "pa" (Pascal), "bar", "psi" (PSI), or "torr" (Torr). The function should convert the `value` from the `from_unit` to the `to_unit` and return the converted value. If the `from_unit` or `to_unit` is not one of the allowed strings, the function should raise an exception with an error message indicating that the unit is invalid.
"""

# Conversions to pascal
conversions_to_pascal = {
    "pa": 1,
    "bar": 100000,
    "psi": 6894.76,
    "torr": 133.322
}

# Conversion from pascal to other measurements
def convert_from_pascal(to_unit, value):
    if to_unit not in conversions_to_pascal:
        raise Exception('Invalid unit: ' + to_unit)
    return value / conversions_to_pascal[to_unit]

# Complete conversion process beginning from a certain measurement moving the value to pascal then to the desired measurement
def convert_pressure(from_unit, to_unit, value):
    if from_unit not in conversions_to_pascal:
        raise Exception('Invalid unit: ' + from_unit)
    value_in_pascal = value * conversions_to_pascal[from_unit]
    return convert_from_pascal(to_unit, value_in_pascal)