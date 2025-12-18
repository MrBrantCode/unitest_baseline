"""
QUESTION:
### Description
As hex values can include letters `A` through to `F`, certain English words can be spelled out, such as `CAFE`, `BEEF`, or `FACADE`.
This vocabulary can be extended by using numbers to represent other letters, such as `5EAF00D`, or `DEC0DE5`.

Given a string, your task is to return the decimal sum of all words in the string that can be interpreted as such hex values.


### Example

Working with the string `BAG OF BEES`:  
* `BAG` ==> `0` as it is not a valid hex value  
* `OF` ==> `0F` ==> `15`  
* `BEES` ==> `BEE5` ==> `48869`

So `hex_word_sum('BAG OF BEES')` returns the sum of these, `48884`.


### Notes
* Inputs are all uppercase and contain no punctuation
* `0` can be substituted for `O`
* `5` can be substituted for `S`
"""

def hex_word_sum(s: str) -> int:
    # Translate 'O' to '0' and 'S' to '5'
    translated_s = s.translate(str.maketrans('OS', '05'))
    
    # Split the string into words
    words = translated_s.split()
    
    # Calculate the sum of valid hex values
    hex_sum = sum((int(w, 16) for w in words if set(w) <= set('0123456789ABCDEF')))
    
    return hex_sum