"""
QUESTION:
Comprised of a team of five incredibly brilliant women, "The ladies of ENIAC" were the first “computors” working at the University of Pennsylvania’s Moore School of Engineering (1945). Through their contributions, we gained the first software application and the first programming classes! The ladies of ENIAC were inducted into the WITI Hall of Fame in 1997!

Write a function which reveals "The ladies of ENIAC" names, so that you too can add them to your own hall of tech fame!

To keep: only alpha characters, space characters and exclamation marks.  
To remove: numbers and these characters: ```%$&/£?@```

Result should be all in uppercase.
"""

import re

def clean_and_format_name(name: str) -> str:
    """
    Cleans and formats the input name string by keeping only alphabetic characters, spaces, and exclamation marks,
    and converting the result to uppercase.

    Parameters:
    name (str): The input string to be cleaned and formatted.

    Returns:
    str: The cleaned and formatted string.
    """
    return ''.join(re.findall('[A-Z\\s!]+', name.upper()))