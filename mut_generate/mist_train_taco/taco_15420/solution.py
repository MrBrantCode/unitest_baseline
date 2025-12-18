"""
QUESTION:
Much cooler than your run-of-the-mill Fibonacci numbers, the Triple Shiftian are so defined: `T[n] = 4 * T[n-1] - 5 * T[n-2] + 3 * T[n-3]`.

You are asked to create a function which accept a base with the first 3 numbers and then returns the nth element.
```python
triple_shiftian([1,1,1],25) == 1219856746
triple_shiftian([1,2,3],25) == 2052198929
triple_shiftian([6,7,2],25) == -2575238999
triple_shiftian([3,2,1],35) == 23471258855679
triple_shiftian([1,9,2],2) ==  2
```
*Note: this is meant to be an interview quiz, so the description is scarce in detail on purpose*

Special thanks to the [first person I met in person here in London just because of CW](http://www.codewars.com/users/webtechalex) and that assisted me during the creation of this kata ;)
"""

def calculate_triple_shiftian(base, n):
    # Ensure the base list has exactly three elements
    if len(base) != 3:
        raise ValueError("The base list must contain exactly three elements.")
    
    # If n is one of the first three elements, return the corresponding base value
    if n < 3:
        return base[n]
    
    # Initialize the sequence with the base values
    T = base[:]
    
    # Calculate the sequence up to the nth element
    for i in range(3, n + 1):
        next_value = 4 * T[i - 1] - 5 * T[i - 2] + 3 * T[i - 3]
        T.append(next_value)
    
    # Return the nth element
    return T[n]