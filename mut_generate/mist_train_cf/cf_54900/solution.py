"""
QUESTION:
Create a function `convert_temp` that takes three parameters: `scale_from`, `scale_to`, and `temp`. The function should convert the given temperature `temp` from the `scale_from` to the `scale_to` scale. The temperature scales can be 'Celsius', 'Fahrenheit', or 'Kelvin'. If the `scale_from` or `scale_to` is not one of these three scales, the function should return an error message.
"""

def convert_temp(scale_from, scale_to, temp):
    if scale_from == 'Celsius':
        if scale_to == 'Fahrenheit':
            return temp * 1.8 + 32
        elif scale_to == 'Kelvin':
            return temp + 273.15
        else:
            return 'Unknown scale to convert to!'
    elif scale_from == 'Fahrenheit':
        if scale_to == 'Celsius':
            return (temp - 32) / 1.8
        elif scale_to == 'Kelvin':
            return (temp + 459.67) * 5/9
        else:
            return 'Unknown scale to convert to!'
    elif scale_from == 'Kelvin':
        if scale_to == 'Celsius':
            return temp - 273.15
        elif scale_to == 'Fahrenheit':
            return temp * 9/5 - 459.67
        else:
            return 'Unknown scale to convert to!'
    else:
        return 'Unknown scale to convert from!'