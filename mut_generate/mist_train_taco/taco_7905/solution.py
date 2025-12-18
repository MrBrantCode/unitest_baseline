"""
QUESTION:
ASC Week 1 Challenge 4 (Medium #1) 

Write a function that converts any sentence into a V  A  P  O  R  W  A  V  E sentence. a V  A  P  O  R  W  A  V  E sentence converts all the letters into uppercase, and adds 2 spaces between each letter (or special character) to create this V  A  P  O  R  W  A  V  E effect.

Examples:
```javascript 
  vaporcode("Lets go to the movies") // output => "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
  vaporcode("Why isn't my code working?") // output => "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"
```
```ruby 
  vaporcode("Lets go to the movies") # output => "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
  vaporcode("Why isn't my code working?") # output => "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"
```
```python 
  vaporcode("Lets go to the movies") # output => "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
  vaporcode("Why isn't my code working?") # output => "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"
```
```crystal 
  vaporcode("Lets go to the movies") # output => "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
  vaporcode("Why isn't my code working?") # output => "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"
```
```cpp 
  vaporcode("Lets go to the movies") // output => "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
  vaporcode("Why isn't my code working?") // output => "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"
```
```haskell 
  vaporcode "Lets go to the movies" 
  -- output => "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
  vaporcode "Why isn't my code working?" 
  -- output => "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"
```
"""

def vaporwave_transform(sentence: str) -> str:
    """
    Converts a given sentence into a V  A  P  O  R  W  A  V  E sentence.

    This function converts all the letters in the input sentence to uppercase
    and adds 2 spaces between each letter (or special character) to create the
    V  A  P  O  R  W  A  V  E effect.

    Parameters:
    sentence (str): The input sentence to be transformed.

    Returns:
    str: The transformed V  A  P  O  R  W  A  V  E sentence.
    """
    # Remove all spaces and convert to uppercase
    transformed_sentence = sentence.replace(' ', '').upper()
    # Join each character with two spaces in between
    vaporwave_sentence = '  '.join(transformed_sentence)
    return vaporwave_sentence