"""
QUESTION:
You've purchased a ready-meal from the supermarket.

The packaging says that you should microwave it for 4 minutes and 20 seconds, based on a 600W microwave.

Oh no, your microwave is 800W! How long should you cook this for?!

___

# Input

You'll be given 4 arguments:

## 1. needed power
The power of the needed microwave.  
Example: `"600W"`

## 2. minutes
The number of minutes shown on the package.  
Example: `4`

## 3. seconds
The number of seconds shown on the package.  
Example: `20`

## 4. power
The power of your microwave.  
Example: `"800W"`

___

# Output
The amount of time you should cook the meal for formatted as a string.  
Example: `"3 minutes 15 seconds"`

Note: the result should be rounded up.
```
59.2 sec  -->  60 sec  -->  return "1 minute 0 seconds"
```

___


## All comments/feedback/translations appreciated.
"""

import math

def calculate_adjusted_cooking_time(needed_power, minutes, seconds, power):
    # Convert the power strings to integers (excluding the 'W')
    needed_power_value = int(needed_power[:-1])
    power_value = int(power[:-1])
    
    # Calculate the total time in seconds for the needed power
    total_time_needed_power = 60 * minutes + seconds
    
    # Calculate the adjusted time in seconds for the actual power
    adjusted_time_seconds = math.ceil(total_time_needed_power * needed_power_value / power_value)
    
    # Convert the adjusted time back to minutes and seconds
    adjusted_minutes = adjusted_time_seconds // 60
    adjusted_seconds = adjusted_time_seconds % 60
    
    # Return the formatted string
    return f"{adjusted_minutes} minutes {adjusted_seconds} seconds"