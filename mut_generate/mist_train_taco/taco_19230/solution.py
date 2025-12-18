"""
QUESTION:
There was once young lass called Mary,  

Whose jokes were occasionally scary.  

On this April's Fool  

Fixed limerick rules  

Allowed her to trip the unwary.



Can she fill all the lines

To work at all times?

On juggling the words

Right around two-thirds

She nearly ran out of rhymes.




-----Input-----

The input contains a single integer $a$ ($4 \le a \le 998$). Not every integer in the range is a valid input for the problem; you are guaranteed that the input will be a valid integer.


-----Output-----

Output a single number.


-----Examples-----
Input
35

Output
57

Input
57

Output
319

Input
391

Output
1723
"""

def find_limerick_number(a: int) -> str:
    """
    Finds and returns a specific number based on the input integer 'a' according to the limerick rules.

    Parameters:
    a (int): An integer in the range [4, 998].

    Returns:
    str: A string representing the output number.
    """
    divisor = 2
    while a % divisor != 0:
        divisor += 1
    
    quotient = a // divisor
    result = ''
    
    if divisor < quotient:
        result += f'{divisor}'
        result += f'{quotient}'
    else:
        result += f'{quotient}'
        result += f'{divisor}'
    
    return result