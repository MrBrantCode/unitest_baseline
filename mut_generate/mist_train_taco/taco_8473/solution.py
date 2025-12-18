"""
QUESTION:
Hofstadter sequences are a family of related integer sequences, among which the first ones were described by an American professor Douglas Hofstadter in his book Gödel, Escher, Bach. 

### Task
Today we will be implementing the rather chaotic recursive sequence of integers called Hofstadter Q.
The Hofstadter Q is defined as:

As the author states in the aforementioned book:It is reminiscent of the Fibonacci definition in that each new value is a sum of two
previous values-but not of the immediately previous two values. Instead, the two
immediately previous values tell how far to count back to obtain the numbers to be added
to make the new value.
The function produces the starting sequence:  
`1, 1, 2, 3, 3, 4, 5, 5, 6 . . .`  
Test info: 100 random tests, n is always positive
Good luck!
"""

def hofstadter_Q(n):
    # Initialize the sequence with the first two values
    if not hasattr(hofstadter_Q, 'seq'):
        hofstadter_Q.seq = [None, 1, 1]
    
    # Try to return the value from the sequence if it has already been computed
    try:
        return hofstadter_Q.seq[n]
    except IndexError:
        # Compute the value recursively and store it in the sequence
        ans = hofstadter_Q(n - hofstadter_Q(n - 1)) + hofstadter_Q(n - hofstadter_Q(n - 2))
        hofstadter_Q.seq.append(ans)
        return ans