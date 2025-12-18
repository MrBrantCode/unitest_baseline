"""
QUESTION:
## Task
In this kata you'll be given a string of English digits "collapsed" together, like this:

`zeronineoneoneeighttwoseventhreesixfourtwofive`

Your task is to split the string back to digits:

`zero nine one one eight two seven three six four two five`

## Examples
```
three -> three
eightsix -> eight six
fivefourseven -> five four seven
ninethreesixthree -> nine three six three
fivethreefivesixthreenineonesevenoneeight -> five three five six three nine one seven one eight
```
"""

import re

def uncollapse_digits(digits: str) -> str:
    """
    Splits a string of collapsed English digits into individual digits separated by spaces.

    Parameters:
    digits (str): A string containing the collapsed English digits.

    Returns:
    str: A string where each English digit is separated by a space.
    """
    return ' '.join(re.findall('zero|one|two|three|four|five|six|seven|eight|nine', digits))