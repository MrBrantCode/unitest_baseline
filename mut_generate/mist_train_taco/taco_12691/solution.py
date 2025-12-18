"""
QUESTION:
You are given a string of numbers between 0-9. Find the average of these numbers and return it as a floored whole number (ie: no decimal places) written out as a string. Eg:

"zero nine five two" -> "four"

If the string is empty or includes a number greater than 9, return "n/a"
"""

def average_string(s):
    N = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    try:
        # Split the input string into words
        words = s.split()
        
        # Convert words to their corresponding indices in N
        numbers = [N.index(word) for word in words]
        
        # Calculate the floored average of the numbers
        average = sum(numbers) // len(words)
        
        # Return the corresponding word from N
        return N[average]
    
    except (ZeroDivisionError, ValueError):
        # Handle cases where the string is empty or contains invalid words
        return 'n/a'