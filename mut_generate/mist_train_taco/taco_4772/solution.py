"""
QUESTION:
Young Sheldon is given the task to teach Chemistry to his brother Georgie. After teaching him how to find total atomic weight, Sheldon gives him some formulas which consist of $x$, $y$ and $z$ atoms as an assignment. 
You already know that Georgie doesn't like Chemistry, so he want you to help him solve this assignment.
Let the chemical formula be given by the string $S$. It consists of any combination of x, y and z with some value associated with it as well as parenthesis to encapsulate any combination. Moreover, the atomic weight of x, y and z are 2, 4 and 10 respectively.
You are supposed to find the total atomic weight of the element represented by the given formula.
For example, for the formula $(x_2y_2)_3z$, given string $S$ will be: $(x2y2)3z$. Hence, substituting values of x, y and z, total atomic weight will be 
$(2*2+4*2)*3 + 10 = 46$.

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains of a single line of input $S$. 

-----Output:-----
For each testcase, output in a single line, the total atomic weight.

-----Constraints-----
- $1 \leq T \leq 100$
- Length of string $S \leq 100$
- String contains $x, y, z, 1, 2,..., 9$ and parenthesis

-----Sample Input:-----
2
(xy)2
x(x2y)3(z)2

-----Sample Output:-----
12
46
"""

def calculate_atomic_weight(formula: str) -> int:
    s = list(formula.strip())
    i = 0
    while i < len(s) - 1:
        if s[i].isalpha() or s[i] == ')':
            if s[i + 1].isdigit():
                if i + 2 >= len(s) or s[i + 2] == ')':
                    s = s[:i + 1] + ['*', s[i + 1]] + s[i + 2:]
                else:
                    s = s[:i + 1] + ['*', s[i + 1], '+'] + s[i + 2:]
                i += 1
            elif s[i + 1].isalpha() or s[i + 1] == '(':
                s = s[:i + 1] + ['+'] + s[i + 1:]
        i += 1
    s = ''.join(s)
    s = s.strip('+')
    x = 2
    y = 4
    z = 10
    total_weight = eval(s)
    return total_weight