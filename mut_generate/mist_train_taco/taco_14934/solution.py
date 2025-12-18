"""
QUESTION:
When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) component values for a color. Implement a function that meets these requirements:

+ Accepts a case-insensitive hexadecimal color string as its parameter (ex. `"#FF9933"` or `"#ff9933"`)
+ Returns an object with the structure `{r: 255, g: 153, b: 51}` where *r*, *g*, and *b* range from 0 through 255

**Note:** your implementation does not need to support the shorthand form of hexadecimal notation (ie `"#FFF"`)


## Example

```
"#FF9933" --> {r: 255, g: 153, b: 51}
```
"""

def hex_to_rgb(hex_color: str) -> dict:
    # Ensure the hex color string is in uppercase for consistency
    hex_color = hex_color.upper()
    
    # Extract the RGB components using slicing and convert to integers
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    
    # Return the result as a dictionary
    return {'r': r, 'g': g, 'b': b}