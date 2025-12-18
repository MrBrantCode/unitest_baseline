"""
QUESTION:
Write a function ```convert_temp(temp, from_scale, to_scale)``` converting temperature from one scale to another. 
Return converted temp value. 

Round converted temp value to an integer(!).

Reading: http://en.wikipedia.org/wiki/Conversion_of_units_of_temperature

```
possible scale inputs:
    "C"  for Celsius
    "F"  for Fahrenheit
    "K"  for Kelvin
    "R"  for Rankine
    "De" for Delisle
    "N"  for Newton
    "Re" for Réaumur
    "Ro" for Rømer
```

```temp``` is a number, ```from_scale``` and ```to_scale``` are strings. 

```python
convert_temp(   100, "C",  "F") # => 212
convert_temp(    40, "Re", "C") # => 50
convert_temp(    60, "De", "F") # => 140
convert_temp(373.15, "K",  "N") # => 33
convert_temp(   666, "K",  "K") # => 666
```
"""

def convert_temperature(temp, from_scale, to_scale):
    TO_KELVIN = {
        'C': (1, 273.15),
        'F': (5.0 / 9, 459.67 * 5.0 / 9),
        'R': (5.0 / 9, 0),
        'De': (-2.0 / 3, 373.15),
        'N': (100.0 / 33, 273.15),
        'Re': (5.0 / 4, 273.15),
        'Ro': (40.0 / 21, -7.5 * 40 / 21 + 273.15)
    }
    
    if from_scale == to_scale:
        return int(round(temp))
    
    if from_scale != 'K':
        (a, b) = TO_KELVIN[from_scale]
        temp = a * temp + b
        if to_scale == 'K':
            return int(round(temp))
    
    (a, b) = TO_KELVIN[to_scale]
    return int(round((temp - b) / a))