"""
QUESTION:
Mr. A wants to get to the destination on the Yamanote line.

After getting on the train, Mr. A gets up for a minute and sleeps for b minutes repeatedly. It is c minutes after boarding to the destination, and you can get off if you are awake at this time, but on the contrary, if you are sleeping, you will miss it. Also, Mr. A will continue to take the same train even if he overtakes it, and the train will take 60 minutes to go around the Yamanote line. Therefore, Mr. A will arrive at the destination after 60t + c (t is a non-negative integer) minutes.

How many minutes will A be able to reach his destination? Output -1 when it is unreachable. However, if the time you arrive at your destination is the boundary between the time you are sleeping and the time you are awake, you can get off.

Constraints

* 0 <a, b, c <60

Input

The input is given in one line in the following format.


a b c


The input consists of three integers a, b, c.

a is the time you are awake, b is the time you are sleeping, and c is the time it takes to get to your destination after boarding. The unit of a, b, and c is minutes.

Output

If you can reach your destination, output the time it takes to reach your destination. Otherwise, output -1.

Examples

Input

10 10 5


Output

5


Input

50 40 51


Output

111


Input

20 20 20


Output

20


Input

30 30 40


Output

-1
"""

def calculate_arrival_time(a: int, b: int, c: int) -> int:
    if a + b == 60 and c > a:
        return -1
    
    right = 0
    left = a
    i = 0
    
    while True:
        if left >= c and c >= right:
            return c
        if left + b > c and c > right + a:
            c += 60
        
        left += b + a
        right += a + b
        i += 1
        
        if i > 60:
            return -1