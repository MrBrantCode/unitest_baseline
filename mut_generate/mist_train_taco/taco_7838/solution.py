"""
QUESTION:
Petya learned a new programming language CALPAS. A program in this language always takes one non-negative integer and returns one non-negative integer as well.

In the language, there are only three commands: apply a bitwise operation AND, OR or XOR with a given constant to the current integer. A program can contain an arbitrary sequence of these operations with arbitrary constants from 0 to 1023. When the program is run, all operations are applied (in the given order) to the argument and in the end the result integer is returned.

Petya wrote a program in this language, but it turned out to be too long. Write a program in CALPAS that does the same thing as the Petya's program, and consists of no more than 5 lines. Your program should return the same integer as Petya's program for all arguments from 0 to 1023.


-----Input-----

The first line contains an integer n (1 ≤ n ≤ 5·10^5) — the number of lines.

Next n lines contain commands. A command consists of a character that represents the operation ("&", "|" or "^" for AND, OR or XOR respectively), and the constant x_{i} 0 ≤ x_{i} ≤ 1023.


-----Output-----

Output an integer k (0 ≤ k ≤ 5) — the length of your program.

Next k lines must contain commands in the same format as in the input.


-----Examples-----
Input
3
| 3
^ 2
| 1

Output
2
| 3
^ 2

Input
3
& 1
& 3
& 5

Output
1
& 1

Input
3
^ 1
^ 2
^ 3

Output
0



-----Note-----

You can read about bitwise operations in https://en.wikipedia.org/wiki/Bitwise_operation.

Second sample:

Let x be an input of the Petya's program. It's output is ((x&1)&3)&5 = x&(1&3&5) = x&1. So these two programs always give the same outputs.
"""

def optimize_calpas_program(n, com):
    """
    Optimizes a CALPAS program to reduce the number of commands to at most 5.

    Parameters:
    n (int): The number of commands in the original program.
    com (list of tuples): A list of commands where each command is a tuple (operation, constant).
                          Operation is a string ("&", "|", "^") and constant is an integer (0 ≤ constant ≤ 1023).

    Returns:
    tuple: A tuple containing the number of optimized commands (k) and a list of optimized commands.
           Each optimized command is a tuple (operation, constant).
    """
    (AND, OR, XOR) = ([], [], [])
    for i in range(10):
        res1 = 0
        res2 = 1
        for (s, n) in com:
            b = n >> i & 1
            if s == '&':
                res1 &= b
                res2 &= b
            elif s == '|':
                res1 |= b
                res2 |= b
            elif s == '^':
                res1 ^= b
                res2 ^= b
        if (res1, res2) == (0, 0):
            AND.append(i)
        elif (res1, res2) == (1, 1):
            OR.append(i)
        elif (res1, res2) == (1, 0):
            XOR.append(i)
    
    AND_n = 0
    for i in range(10):
        if i not in AND:
            AND_n += 2 ** i
    
    OR_n = 0
    for i in OR:
        OR_n += 2 ** i
    
    XOR_n = 0
    for i in XOR:
        XOR_n += 2 ** i
    
    optimized_commands = []
    if AND_n != 1023:
        optimized_commands.append(('&', AND_n))
    if OR_n != 0:
        optimized_commands.append(('|', OR_n))
    if XOR_n != 0:
        optimized_commands.append(('^', XOR_n))
    
    k = len(optimized_commands)
    return k, optimized_commands