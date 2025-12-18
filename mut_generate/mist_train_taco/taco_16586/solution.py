"""
QUESTION:
You are given string s consists of opening and closing brackets of four kinds <>, {}, [], (). There are two types of brackets: opening and closing. You can replace any bracket by another of the same type. For example, you can replace < by the bracket {, but you can't replace it by ) or >.

The following definition of a regular bracket sequence is well-known, so you can be familiar with it.

Let's define a regular bracket sequence (RBS). Empty string is RBS. Let s_1 and s_2 be a RBS then the strings <s_1>s_2, {s_1}s_2, [s_1]s_2, (s_1)s_2 are also RBS.

For example the string "[[(){}]<>]" is RBS, but the strings "[)()" and "][()()" are not.

Determine the least number of replaces to make the string s RBS.


-----Input-----

The only line contains a non empty string s, consisting of only opening and closing brackets of four kinds. The length of s does not exceed 10^6.


-----Output-----

If it's impossible to get RBS from s print Impossible.

Otherwise print the least number of replaces needed to get RBS from s.


-----Examples-----
Input
[<}){}

Output
2
Input
{()}[]

Output
0
Input
]]

Output
Impossible
"""

def min_replacements_to_rbs(s: str) -> int or str:
    dic = {'{': 1, '}': -1, '<': 2, '>': -2, '[': 3, ']': -3, '(': 4, ')': -4}
    stack = []
    count = 0
    n = 0
    
    for x in s:
        if dic[x] < 0:
            if n == 0:
                return "Impossible"
            if dic[stack[n - 1]] + dic[x] != 0:
                count += 1
            stack.pop()
            n -= 1
        else:
            stack.append(x)
            n += 1
    
    if n != 0:
        return "Impossible"
    else:
        return count