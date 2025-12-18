"""
QUESTION:
Two integers A and B are the inputs. Write a program to find GCD and LCM of A and B.

-----Input-----

The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer A and B. 

-----Output-----
Display the GCD and LCM of A and B separated by space respectively. The answer for each test case must be displayed in a new line.

-----Constraints-----
- 1 ≤ T ≤ 1000
- 1 ≤ A,B ≤ 1000000

-----Example-----
Input
3 
120 140
10213 312
10 30

Output

20 840
1 3186456
10 30
"""

def compute_gcd_lcm(A: int, B: int) -> tuple:
    """
    Compute the Greatest Common Divisor (GCD) and Least Common Multiple (LCM) of two integers A and B.

    Parameters:
    A (int): The first integer.
    B (int): The second integer.

    Returns:
    tuple: A tuple containing the GCD and LCM of A and B.
    """
    def GCD(x, y):
        while y:
            (x, y) = (y, x % y)
        return x

    def LCM(x, y):
        lcm = x * y // GCD(x, y)
        return lcm

    gcd_value = GCD(A, B)
    lcm_value = LCM(A, B)
    
    return (gcd_value, lcm_value)