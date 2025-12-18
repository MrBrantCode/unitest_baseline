"""
QUESTION:
You're looking through different hex codes, and having trouble telling the difference between  #000001  and  #100000 

We need a way to tell which is red, and which is blue!

That's where you create ```hex_color()```!

It should read an RGB input, and return whichever value (red, blue, or green) is of greatest concentration!

But, if multiple colors are of equal concentration, you should return their mix!

```python
red + blue = magenta

green + red = yellow

blue + green = cyan

red + blue + green = white
```

One last thing, if the string given is empty, or has all 0's, return black!

Examples:
```python
hex_color('087 255 054') == 'green'
hex_color('181 181 170') == 'yellow'
hex_color('000 000 000') == 'black'
hex_color('001 001 001') == 'white'
```
"""

def determine_dominant_color(rgb_string: str) -> str:
    # Define the color mappings
    colors = {
        (1, 0, 0): 'red',
        (0, 1, 0): 'green',
        (0, 0, 1): 'blue',
        (1, 0, 1): 'magenta',
        (1, 1, 0): 'yellow',
        (0, 1, 1): 'cyan',
        (1, 1, 1): 'white'
    }
    
    # Handle empty input or all zeros case
    if not rgb_string or rgb_string.strip() == '0 0 0':
        return 'black'
    
    # Split the input string into individual RGB values and convert to integers
    items = [int(c) for c in rgb_string.split()]
    
    # Find the maximum value among the RGB values
    m = max(items)
    
    # Determine the dominant color or mixed color
    if m == 0:
        return 'black'
    else:
        return colors[tuple((i == m for i in items))]