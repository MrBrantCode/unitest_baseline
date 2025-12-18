"""
QUESTION:
![](http://www.grindtv.com/wp-content/uploads/2015/08/drone.jpg)

The other day I saw an amazing video where a guy hacked some wifi controlled lightbulbs by flying a drone past them. Brilliant.

In this kata we will recreate that stunt... sort of.

You will be given two strings: `lamps` and `drone`. `lamps` represents a row of lamps, currently off, each represented by `x`. When these lamps are on, they should be represented by `o`.

The `drone` string represents the position of the drone `T` (any better suggestion for character??) and its flight path up until this point `=`. The drone always flies left to right, and always begins at the start of the row of lamps. Anywhere the drone has flown, including its current position, will result in the lamp at that position switching on.

Return the resulting `lamps` string. See example tests for more clarity.
"""

def turn_on_lamps(lamps, drone):
    # Calculate the number of lamps to turn on
    num_lamps_to_turn_on = drone.count('=') + 1
    
    # Replace the appropriate number of 'x' with 'o' in the lamps string
    return lamps.replace('x', 'o', num_lamps_to_turn_on)