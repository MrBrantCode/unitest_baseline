"""
QUESTION:
Write a function taking in a string like `WOW this is REALLY          amazing` and returning `Wow this is really amazing`. String should be capitalized and properly spaced. Using `re` and `string` is not allowed.

Examples:

```python
filter_words('HELLO CAN YOU HEAR ME') #=> Hello can you hear me
filter_words('now THIS is REALLY interesting') #=> Now this is really interesting
filter_words('THAT was EXTRAORDINARY!') #=> That was extraordinary!
```
"""

def clean_and_format_string(input_string):
    """
    Cleans and formats the input string by capitalizing the first letter of the first word,
    converting the rest of the string to lowercase, and ensuring proper spacing between words.

    Parameters:
    input_string (str): The input string to be cleaned and formatted.

    Returns:
    str: The cleaned and formatted string.
    """
    return ' '.join(input_string.capitalize().split())