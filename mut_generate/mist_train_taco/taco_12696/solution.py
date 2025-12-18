"""
QUESTION:
Manipulating numbers is at the core of a programmer's job. To test how well you know their properties, you are asked to solve the following problem.

You are given $n$ non-negative integers $a_1$, $a_2$, ..., $a_n$. You want to know whether it's possible to construct a new integer using all the digits of these numbers such that it would be divisible by $3$. You can reorder the digits as you want. The resulting number can contain leading zeros.

For example, consider the numbers $50,40,90$ from which you have to construct a new integer as described above. Numerous arrangements of digits are possible; but we have illustrated one below. 

Complete the function canConstruct which takes an integer array as input and return "Yes" or "No" based on whether or not the required integer can be formed.

Input Format

The first line contains a single integer ${t}}$ denoting the number of queries. The following lines describe the queries.

Each query is described in two lines. The first of these lines contains a single integer $n$. The second contains $n$ space-separated integers $a_1$, $a_2$, ..., $a_n$.

Constraints

$1\leq t\leq100$
$1\leq n\leq100$
$1\leq a_i\leq10^9$

Subtasks

For 33.33% of the total score:

$n=1$
$1\leq a_1\leq10^6$

Output Format

For each query, print a single line containing "Yes" if it's possible to construct such integer and "No" otherwise.

Sample Input 0
3
1
9
3
40 50 90
2
1 4

Sample Output 0
Yes
Yes
No

Explanation 0

In the first example, $\mbox{9}$ is divisible by $3$, so the answer is "Yes".

In the second example you can construct the number ${005490}$ which is divisible by $3$, so the answer is "Yes". Note that there may be other numbers you can construct, some of which are shown in the challenge statement.

In the third example, the only possible numbers are ${14}$ and ${41}$, but both of them are not divisible by $3$, so the answer is "No".
"""

def can_construct_divisible_by_3(a: list[int]) -> str:
    """
    Determines if it's possible to construct a number using all the digits of the given integers
    such that the number is divisible by 3.

    Parameters:
    a (list[int]): A list of non-negative integers.

    Returns:
    str: "Yes" if such a number can be constructed, otherwise "No".
    """
    return 'Yes' if not sum(a) % 3 else 'No'