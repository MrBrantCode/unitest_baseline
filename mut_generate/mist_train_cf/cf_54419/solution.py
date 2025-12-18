"""
QUESTION:
Design a function named `interpret_symbol` that interprets five uncommon symbols "#", "@", "&", "$", and "*" from a given codebook and returns the corresponding interpretation. The function should also include error handling to signal when an unrecognized symbol is encountered and handle it gracefully by printing an error message without crashing the program.

The codebook is a dictionary with the symbols as keys and their interpretations as values:

```python
codebook = {
    "#" : "symbol1",
    "@" : "symbol2",
    "&" : "symbol3",
    "$" : "symbol4",
    "*" : "symbol5"
}
```
"""

codebook = {
    "#" : "symbol1",
    "@" : "symbol2",
    "&" : "symbol3",
    "$" : "symbol4",
    "*" : "symbol5"
}

def interpret_symbol(symbol):
    try:
        return "Interpreted Symbol: " + codebook[symbol]
    except KeyError:
        return error_handling(symbol)

def error_handling(symbol):
    unrecognized_symbol = "Unrecognized Symbol: " + symbol
    print(unrecognized_symbol)
    return unrecognized_symbol