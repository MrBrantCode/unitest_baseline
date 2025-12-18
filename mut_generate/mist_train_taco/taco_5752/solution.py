"""
QUESTION:
There exists an island called Arpa’s land, some beautiful girls live there, as ugly ones do.

Mehrdad wants to become minister of Arpa’s land. Arpa has prepared an exam. Exam has only one question, given n, print the last digit of 1378^{n}. 

 [Image] 

Mehrdad has become quite confused and wants you to help him. Please help, although it's a naive cheat.


-----Input-----

The single line of input contains one integer n (0  ≤  n  ≤  10^9).


-----Output-----

Print single integer — the last digit of 1378^{n}.


-----Examples-----
Input
1

Output
8
Input
2

Output
4


-----Note-----

In the first example, last digit of 1378^1 = 1378 is 8.

In the second example, last digit of 1378^2 = 1378·1378 = 1898884 is 4.
"""

def last_digit_of_power(n: int) -> int:
    """
    Calculate the last digit of 1378 raised to the power of n.

    Parameters:
    n (int): The power to which 1378 is raised.

    Returns:
    int: The last digit of 1378^n.
    """
    if n == 0:
        return 1
    
    arr = [8, 4, 2, 6]
    return arr[(n - 1) % 4]