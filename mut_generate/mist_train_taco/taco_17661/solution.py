"""
QUESTION:
Chuck has lost count of how many asses he has kicked...

Chuck stopped counting at 100,000 because he prefers to kick things in the face instead of counting. That's just who he is.

To stop having to count like a mere mortal chuck developed his own special code using the hairs on his beard. You do not need to know the details of how it works, you simply need to know that the format is as follows: 'A8A8A8A8A8.-A%8.88.'

In Chuck's code, 'A' can be any capital letter and '8' can be any number 0-9 and any %, - or . symbols must not be changed.

Your task, to stop Chuck beating your ass with his little finger, is to use regex to verify if the number is a genuine Chuck score. If not it's probably some crap made up by his nemesis Bruce Lee. Return true if the provided count passes, and false if it does not.  

```Javascript
Example:
     'A8A8A8A8A8.-A%8.88.' <- don't forget final full stop :D\n
Tests:
     'A2B8T1Q9W4.-F%5.34.' == true;
     'a2B8T1Q9W4.-F%5.34.' == false; (small letter)
     'A2B8T1Q9W4.-F%5.3B.' == false; (last char should be number) 
     'A2B8T1Q9W4.£F&5.34.' == false; (symbol changed from - and %)
 ```

The pattern only needs to appear within the text. The full input can be longer, i.e. the pattern can be surrounded by other characters... Chuck loves to be surrounded!

Ready, steady, VERIFY!!
"""

from re import search

def is_genuine_chuck_score(code: str) -> bool:
    """
    Verifies if the provided code matches the genuine Chuck score pattern.

    Parameters:
    code (str): The string to be verified.

    Returns:
    bool: True if the code matches the pattern, False otherwise.
    """
    return bool(search(r'(?:[A-Z]\d){5}\.-[A-Z]%\d\.\d{2}\.', code))