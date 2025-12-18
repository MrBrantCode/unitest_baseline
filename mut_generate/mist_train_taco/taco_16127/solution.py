"""
QUESTION:
# Task

You are given a function that should insert an asterisk (`*`) between every pair of **even digits** in the given input, and return it as a string. If the input is a sequence, concat the elements first as a string. 


## Input

The input can be an integer, a string of digits or a sequence containing integers only. 


## Output

Return a string. 


## Examples
```
5312708     -->  "531270*8"
"0000"      -->  "0*0*0*0"
[1, 4, 64]  -->  "14*6*4"
```

Have fun!
"""

import re

def insert_asterisks_between_evens(input_data):
    # Convert input to a string if it's an integer or a list of integers
    if isinstance(input_data, int):
        input_data = str(input_data)
    elif isinstance(input_data, list):
        input_data = ''.join(map(str, input_data))
    
    # Use regex to insert asterisks between every pair of even digits
    return re.sub('(?<=[02468])(?=[02468])', '*', input_data)