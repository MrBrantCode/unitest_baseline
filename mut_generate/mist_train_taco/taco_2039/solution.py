"""
QUESTION:
# How many urinals are free?
In men's public toilets with urinals, there is this unwritten rule that you leave at least one urinal free
between you and the next person peeing. 
For example if there are 3 urinals and one person is already peeing in the left one, you will choose the
urinal on the right and not the one in the middle.
That means that a maximum of 3 people can pee at the same time on public toilets with 
5 urinals when following this rule (Only 2 if the first person pees into urinal 2 or 4).

![Imgur Urinals](https://i.imgur.com/imZE6xm.png)

## Your task:
You need to write a function that returns the maximum of free urinals as an integer according to the unwritten rule.

### Input
A String containing 1s and 0s (Example: `10001`) (1 <= Length <= 20)  
A one stands for a taken urinal and a zero for a free one. 

### Examples

`10001` returns 1 (10101)  
`1001` returns 0 (1001)  
`00000` returns 3 (10101)  
`0000` returns 2 (1001)  
`01000` returns 1 (01010 or 01001) 

### Note
When there is already a mistake in the input string (for example `011`), then return `-1`

Have fun and don't pee into the wrong urinal ;)
"""

def calculate_free_urinals(urinals: str) -> int:
    # Check for invalid input where two '1's are adjacent
    if '11' in urinals:
        return -1
    
    # Add padding to handle edge cases
    padded_urinals = f'0{urinals}0'
    
    # Split by '1' to get segments of '0's
    segments = padded_urinals.split('1')
    
    # Calculate the number of free urinals that can be added in each segment
    free_urinals = sum(((len(segment) - 1) // 2 for segment in segments))
    
    return free_urinals