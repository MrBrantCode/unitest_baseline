"""
QUESTION:
FizzBuzz is often one of the first programming puzzles people learn. Now undo it with reverse FizzBuzz!

Write a function that accepts a string, which will always be a valid section of FizzBuzz. Your function must return an array that contains the numbers in order to generate the given section of FizzBuzz.

Notes:
- If the sequence can appear multiple times within FizzBuzz, return the numbers that generate the first instance of that sequence.
- All numbers in the sequence will be greater than zero.
- You will never receive an empty sequence.


## Examples
```
reverse_fizzbuzz("1 2 Fizz 4 Buzz")        -->  [1, 2, 3, 4, 5]
reverse_fizzbuzz("Fizz 688 689 FizzBuzz")  -->  [687, 688, 689, 690]
reverse_fizzbuzz("Fizz Buzz")              -->  [9, 10]
```
"""

def reverse_fizzbuzz(s):
    # Handle specific known cases
    if s == 'Fizz':
        return [3]
    if s == 'Buzz':
        return [5]
    if s == 'Fizz Buzz':
        return [9, 10]
    if s == 'Buzz Fizz':
        return [5, 6]
    if s == 'FizzBuzz':
        return [15]
    
    # Split the input string into a list of words
    s = s.split()
    
    # Find the first digit in the sequence to determine the starting point
    for i in range(len(s)):
        if s[i].isdigit():
            start = int(s[i]) - i
            return list(range(start, start + len(s)))
    
    # If no digit is found, return None (though the problem guarantees a valid input)
    return None