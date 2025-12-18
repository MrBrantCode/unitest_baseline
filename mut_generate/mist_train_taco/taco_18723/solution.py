"""
QUESTION:
You start with a value in dollar form, e.g. $5.00. You must convert this value to a string in which the value is said, like '5 dollars' for example. This should account for ones, cents, zeroes, and negative values. Here are some examples:
```python
dollar_to_speech('$0.00') == '0 dollars.'
dollar_to_speech('$1.00') == '1 dollar.'
dollar_to_speech('$0.01') == '1 cent.'
dollar_to_speech('$5.00') == '5 dollars.'
dollar_to_speech('$20.18') == '20 dollars and 18 cents.'
dollar_to_speech('$-1.00') == 'No negative numbers are allowed!'
```
These examples account for pretty much everything. This kata has many specific outputs, so good luck!
"""

def convert_dollar_to_speech(value: str) -> str:
    if '-' in value:
        return 'No negative numbers are allowed!'
    
    # Remove the dollar sign and split the value into dollars and cents
    (d, c) = (int(n) for n in value.replace('$', '').split('.'))
    
    # Construct the dollar part of the string
    dollars = '{} dollar{}'.format(str(d), 's' if d != 1 else '') if d or not c else ''
    
    # Determine the link between dollars and cents
    link = ' and ' if d and c else ''
    
    # Construct the cent part of the string
    cents = '{} cent{}'.format(str(c), 's' if c != 1 else '') if c else ''
    
    # Combine all parts and return the result
    return '{}{}{}.'.format(dollars, link, cents)