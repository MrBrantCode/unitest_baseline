"""
QUESTION:
Create a function called `unit_conversion` that accepts three parameters: `original_unit`, `target_unit`, and `value`. The function should convert the given `value` from `original_unit` to `target_unit` and return the result. The function should support the following conversions: 
- Inches to Centimeters
- Centimeters to Inches
- Miles to Kilometers
- Kilometers to Miles
- Pounds to Kilograms
- Kilograms to Pounds

The function should adhere to standard conversion rates, handle invalid input, and support floating-point numbers.
"""

def unit_conversion(original_unit, target_unit, value):
    original_unit = original_unit.lower().strip()
    target_unit = target_unit.lower().strip()

    conversion_table = {
        'inches': {'centimeters': 2.54},
        'centimeters': {'inches': 0.393700787},
        'miles': {'kilometers': 1.60934},
        'kilometers': {'miles': 0.621371},
        'pounds': {'kilograms': 0.453592},
        'kilograms': {'pounds': 2.20462},
    }

    try:
        if isinstance(value, (int, float)):
            return value * conversion_table[original_unit][target_unit]

    except KeyError as e:
        print('Invalid unit: ', e)

    except Exception as e:
        print('Unexpected Error: ', e)