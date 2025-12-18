"""
QUESTION:
We have N squares assigned the numbers 1,2,3,\ldots,N. Each square has an integer written on it, and the integer written on Square i is a_i.

How many squares i satisfy both of the following conditions?

* The assigned number, i, is odd.
* The written integer is odd.

Constraints

* All values in input are integers.
* 1 \leq N, a_i \leq 100

Input

Input is given from Standard Input in the following format:


N
a_1 a_2 \cdots a_N


Output

Print the number of squares that satisfy both of the conditions.

Examples

Input

5
1 3 4 5 7


Output

2


Input

15
13 76 46 15 50 98 93 77 31 43 84 90 6 24 14


Output

3
"""

def count_odd_squares(N, a):
    # Initialize a counter for the number of valid squares
    count = 0
    
    # Iterate over the list of numbers
    for i in range(N):
        # Check if the index (1-based) is odd and the number is odd
        if (i + 1) % 2 == 1 and a[i] % 2 == 1:
            count += 1
    
    return count