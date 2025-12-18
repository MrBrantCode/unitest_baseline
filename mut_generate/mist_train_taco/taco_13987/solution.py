"""
QUESTION:
# Task
 You know the slogan `p`, which the agitators have been chanting for quite a while now. Roka has heard this slogan a few times, but he missed almost all of them and grasped only their endings. You know the string `r` that Roka has heard. 
 
 You need to determine what is the `minimal number` of times agitators repeated the slogan `p`, such that Roka could hear `r`.

 It is guaranteed the Roka heard nothing but the endings of the slogan P repeated several times.

# Example

 For `p = "glorytoukraine", r = "ukraineaineaine"`, the output should be `3`.

 The slogan was `"glorytoukraine"`, and Roka heard `"ukraineaineaine"`.
 
 He could hear it as follows: `"ukraine"` + `"aine"` + `"aine"` = `"ukraineaineaine"`.

# Input/Output


 - `[input]` string `p`

  The slogan the agitators chanted, a string of lowecase Latin letters.


 - `[input]` string `r`

  The string of lowercase Latin letters Roka has heard.


 - `[output]` an integer

  The `minimum number` of times the agitators chanted.
"""

import re

def minimal_slogan_repetitions(p: str, r: str) -> int:
    """
    Determine the minimal number of times the agitators repeated the slogan `p`
    such that Roka could hear the string `r`.

    Parameters:
    - p (str): The slogan the agitators chanted.
    - r (str): The string Roka heard, which consists of the endings of the slogan `p` repeated several times.

    Returns:
    - int: The minimal number of times the slogan `p` was repeated.
    """
    # Create a regex pattern that matches all possible suffixes of the slogan `p`
    reg = re.compile('|'.join([p[i:] for i in range(len(p))]))
    
    # Count the number of matches of the pattern in the string `r`
    return len(re.findall(reg, r))