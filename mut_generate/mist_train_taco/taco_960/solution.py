"""
QUESTION:
Implement `String#parse_mana_cost`, which parses [Magic: the Gathering mana costs](http://mtgsalvation.gamepedia.com/Mana_cost) expressed as a string and returns a `Hash` with keys being kinds of mana, and values being the numbers.

Don't include any mana types equal to zero.

Format is:

* optionally natural number representing total amount of generic mana (use key `*`)
* optionally followed by any combination of `w`, `u`, `b`, `r`, `g` (case insensitive in input, return lower case in output), each representing one mana of specific color.

If case of Strings not following specified format, return `nil/null/None`.
"""

import re

def parse_mana_cost(mana):
    # Convert the input string to lowercase to handle case insensitivity
    mana_lower = mana.lower()
    
    # Create a dictionary with counts of each mana type (w, u, b, r, g)
    mana_counts = {c: mana_lower.count(c) for c in 'wubrg' if mana_lower.count(c) > 0}
    
    # Split the string by non-digit characters to find generic mana
    generic_mana_parts = re.split('\\D', mana)
    
    # Check if the input string follows the specified format
    if sum(mana_counts.values()) + sum([len(c) for c in generic_mana_parts]) != len(mana):
        return None
    
    # Calculate the total generic mana
    generic_mana = sum([int(c) for c in generic_mana_parts if c != ''])
    
    # Add the generic mana to the dictionary if it's greater than zero
    if generic_mana > 0:
        mana_counts['*'] = generic_mana
    
    return mana_counts