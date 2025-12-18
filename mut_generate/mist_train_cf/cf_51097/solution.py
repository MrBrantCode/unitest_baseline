"""
QUESTION:
Write a function `filter_strings(symbol, digit, arr)` that filters a given list of strings `arr` to only include strings containing the given `symbol` and the digit `digit`. 

- `symbol` should be a single alphabetical character.
- `digit` should be a single digit number between 0 and 9.
- `arr` should be a list of strings.
- If any of the input types are invalid or out of range, return an error message.
"""

def entance(symbol, digit, arr):
  # Error handling for invalid inputs
  if not isinstance(symbol, str) or not isinstance(digit, int) or not isinstance(arr, list):
    return "Invalid Input"

  if len(symbol) != 1 or not symbol.isalpha():
    return "Symbol should be a single alphabet character"

  if digit < 0 or digit > 9:
    return "Digit should be a single digit number between 0 and 9"

  # Filter the array
  return [x for x in arr if symbol in x and str(digit) in x]