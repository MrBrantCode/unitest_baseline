"""
QUESTION:
Check Tutorial tab to know how to to solve.  

The included code stub will read an integer, $n$, from STDIN.

Without using any string methods, try to print the following:  

$123\cdots n$  

Note that "$\bullet\bullet\bullet\bullet$" represents the consecutive values in between.

Example 

$n=5$

Print the string $12345$.

Input Format

The first line contains an integer $n$.  

Constraints

$1\leq n\leq150$

Output Format

Print the list of integers from $\mbox{1}$ through $n$ as a string, without spaces.

Sample Input 0
3

Sample Output 0
123
"""

def generate_consecutive_string(n: int) -> str:
    result = ""
    for x in range(1, n + 1):
        result += str(x)
    return result