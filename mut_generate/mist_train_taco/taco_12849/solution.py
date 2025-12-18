"""
QUESTION:
## Debug celsius converter

Your friend is traveling abroad to the United States so he wrote a program to convert fahrenheit to celsius. Unfortunately his code has some bugs.

Find the errors in the code to get the celsius converter working properly.

To convert fahrenheit to celsius:
```
celsius = (fahrenheit - 32) * (5/9)
```
```if-not:ruby,typescript
Remember that typically temperatures in the current weather conditions are given in whole numbers. It is possible for temperature sensors to report temperatures with a higher accuracy such as to the nearest tenth. Instrument error though makes this sort of accuracy unreliable for many types of temperature measuring sensors. 
```

```if:ruby
Please round to 5dp (use `.round(5)`)
```

```if:typescript
Please round to 5dp (use `Math.round()`)
```
"""

def convert_fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius and rounds the result to 5 decimal places.

    Parameters:
    fahrenheit (float): The temperature in Fahrenheit to be converted.

    Returns:
    float: The temperature in Celsius, rounded to 5 decimal places.
    """
    celsius = (fahrenheit - 32) * (5.0 / 9.0)
    return round(celsius, 5)