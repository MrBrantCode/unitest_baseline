"""
QUESTION:
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string.
The words in the input String will only contain valid consecutive numbers.


## Examples

```
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
```
"""

def sort_sentence_by_word_number(sentence: str) -> str:
    """
    Sorts the words in the given sentence based on the embedded numbers in each word.

    Parameters:
    - sentence (str): A string containing words with embedded numbers.

    Returns:
    - str: A string where the words are sorted based on the embedded numbers.
    """
    if not sentence:
        return ""
    
    return ' '.join(sorted(sentence.split(), key=lambda x: int(''.join(filter(str.isdigit, x)))))