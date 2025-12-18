"""
QUESTION:
A [Word Square](https://en.wikipedia.org/wiki/Word_square) is a set of words written out in a square grid, such that the same words can be read both horizontally and vertically. The number of words, equal to the number of letters in each word, is known as the *order* of the square.

For example, this is an *order* `5` square found in the ruins of Herculaneum:

![](https://i.gyazo.com/e226262e3ada421d4323369fb6cf66a6.jpg)

Given a string of various uppercase `letters`, check whether a *Word Square* can be formed from it. 

Note that you should use each letter from `letters` the exact number of times it occurs in the string. If a *Word Square* can be formed, return `true`, otherwise return `false`.

__Example__

  * For `letters = "SATORAREPOTENETOPERAROTAS"`, the output should be
  `WordSquare(letters) = true`.
    It is possible to form a *word square* in the example above.

  * For `letters = "AAAAEEEENOOOOPPRRRRSSTTTT"`, (which is sorted form of `"SATORAREPOTENETOPERAROTAS"`), the output should also be
  `WordSquare(letters) = true`.

  * For `letters = "NOTSQUARE"`, the output should be
  `WordSquare(letters) = false`.
  
__Input/Output__

* [input] string letters

  A string of uppercase English letters.
  
  Constraints: `3 ≤ letters.length ≤ 100`.


* [output] boolean

  `true`, if a Word Square can be formed;
  
  `false`, if a Word Square cannot be formed.
"""

from collections import Counter

def can_form_word_square(letters: str) -> bool:
    n = int(len(letters) ** 0.5)
    if n * n != len(letters):
        return False
    
    letter_counts = Counter(letters).values()
    odd_count = sum(1 for count in letter_counts if count % 2 != 0)
    
    return odd_count <= n