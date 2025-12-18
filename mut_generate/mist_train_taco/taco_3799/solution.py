"""
QUESTION:
When Mr. Kay was browsing a certain SNS as usual, the problem that "there are people who can solve IQ150 or more" came to the timeline. Mr. Kay has an IQ of over 150, so he solved the problem in an instant without even looking at it. For him, he doesn't have to work on such a mystery. It is enough to leave it to the computer.

problem

The following mysterious mathematical formula was written in the problem.

* \\ (5 + 3 = 28 \\)
* \\ (9 + 1 = 810 \\)
* \\ (8 + 6 = 214 \\)
* \\ (5 + 4 = 19 \\)
* \\ (2 + 2 = 4 \\)
* \\ (15 + 8 = 723 \\)
* \\ (7 + 9 = -216 \\)
* \\ (3 + 0 = 33 \\)



When thinking about the above operator \\ (+ \\), for a positive integer \\ (a \\) \\ (x \ geq 0, y \ geq 0 \\) and \\ (x + y =) Find the number of integer pairs \\ (x, y \\) such that a \\).

input

A positive integer \\ (a \\) is given on one line.

output

Output the number of pairs \\ ((x, y) \\) that satisfy \\ (a = x + y, x \ geq 0, y \ geq 0 \\) on one line.

Constraint

* \\ (1 \ leq a \ leq 10 ^ 9 (= 1000000000) \\)



Input / output example

Input 1


19


Output 1


1


There is one way of \\ (5 + 4 \\).

Input 2


twenty two


Output 2


2


There are two types: \\ (11 + 11 \\) and \\ (2 + 0 \\).

Input 3


1


Output 3


0


\\ (1 + 0 = 11, 0 + 1 = -11 \\). \\ (1 \\) cannot be generated.

Input 4


101


Output 4


0


Note that \\ (1 --0 \\) is not \\ (101 \\).

Input 5


660233276


Output 5


Four






Example

Input

19


Output

1
"""

def count_valid_pairs(a: int) -> int:
    a_str = str(a)
    ans = 0
    
    for i in range(1, len(a_str)):
        df = a_str[:i]
        sm = a_str[i:]
        
        if sm[0] == '0':
            continue
        
        df = int(df)
        sm = int(sm)
        
        if (df + sm) % 2 == 0 and sm >= df and ((sm - df) % 2 == 0):
            ans += 1
    
    if a % 2 == 0:
        ans += 1
    
    return ans