"""
QUESTION:
There are $5$ cities in the country.
The map of the country is given below.
The tour starts from the red city.

Each road is associated with a character.
Initially, there is an empty string.
Every time a road has been travelled the character associated gets appended to the string.
At the green city either the string can be printed or the tour can be continued.
In the problem, you are given a string tell whether it is possible to print the string while following the rules of the country?

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains a single line of input, a string $ s  $. The string consists only of $0's$ and $1's$.

-----Output:-----
For each testcase, output "YES" or "NO" depending on the input.

-----Constraints-----
- 
$1 \leq T \leq 10000$
- 
$1 \leq length of each string \leq 10000$
- 
$ 1 \leq Summation length \leq 10^5$

-----Sample Input:-----
1
100

-----Sample Output:-----
NO

-----EXPLANATION:-----
"""

def can_print_string_in_tour(s: str) -> str:
    place = 'R'
    for char in s:
        if place == 'R':
            if char == '1':
                place = 'B'
        elif place == 'B':
            if char == '0':
                place = 'Y'
        elif place == 'Y':
            if char == '1':
                place = 'B'
            elif char == '0':
                place = 'P'
        elif place == 'P':
            if char == '1':
                place = 'B'
            elif char == '0':
                place = 'G'
        elif place == 'G':
            if char == '1':
                place = 'B'
            elif char == '0':
                place = 'R'
    if place == 'G':
        return 'YES'
    else:
        return 'NO'