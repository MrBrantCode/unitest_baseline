"""
QUESTION:
There are 32 letters in the Polish alphabet: 9 vowels and 23 consonants. 
 
Your task is to change the letters with diacritics:

```
ą -> a,
ć -> c,
ę -> e,
ł -> l,
ń -> n,
ó -> o,
ś -> s,
ź -> z,
ż -> z
```
and print out the string without the use of the Polish letters.


For example:
```
"Jędrzej Błądziński"  -->  "Jedrzej Bladzinski"
```
"""

def correct_polish_letters(s: str) -> str:
    """
    Replaces Polish letters with diacritics in the input string with their corresponding non-diacritic equivalents.

    Parameters:
    s (str): The input string that may contain Polish letters with diacritics.

    Returns:
    str: The input string with all Polish letters replaced by their corresponding non-diacritic equivalents.
    """
    return s.translate(str.maketrans('ąćęłńóśźż', 'acelnoszz'))