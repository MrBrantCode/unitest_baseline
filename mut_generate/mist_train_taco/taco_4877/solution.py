"""
QUESTION:
You are given a string S, each of whose characters is either '0', '1', or '?'.

The *badness* of a binary string is defined to be the (absolute) difference between the number of 1s and the number of 0s present in it. For example, 001 has badness |1-2| = 1 and 11111 has badness |5-0| = 5.

Your task is to replace every '?' present in S with either '0' or '1', such that the badness of the resulting binary string is minimized.

If there are multiple solutions, you may print any of them.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- Each test case contains two lines.
- The first line of each test case contains an integer N, the number of characters of the string S.
- The second line of each test case contains the string S, whose characters are either '0', '1', or '?'.

------ Output Format ------ 

For each test case, print a single line containing the binary string you obtained by replacing each '?' with either '0' or '1' such that its badness is minimum.

If there are multiple possible strings that minimize badness, you may print any of them.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{5}$
- The sum of $N$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
4
4
?101
4
??10
6
???111
5
1?0?1

----- Sample Output 1 ------ 
0101
1010
000111
11001

----- explanation 1 ------ 
Test Case $1$. There are only two possible strings that can be constructed - $1101$ and $0101$. $1101$ has badness $2$, and $0101$ has badness $0$. Thus, the only possible answer is $0101$.

Test Case $2$. There are four possible strings that can be made, namely $\{0010, 0110, 1010, 1110\}$. Their respective badness values are $\{2, 0, 0, 2\}$. The minimum value here is $0$, attained by both $0110$ and $1010$ - and so either of these strings is a valid answer.

Test Case $3$. There are eight possible strings, of which $000111$ is the only one with minimum badness (that being $0$).

Test Case $4$. There are four possible strings, out of which three of them ($10001$, $10011$, $11001$) have badness $1$, which is minimum. All three of them are possible answers.
"""

def minimize_badness(S: str) -> str:
    """
    Replaces each '?' in the string S with either '0' or '1' to minimize the badness of the resulting binary string.

    Parameters:
    S (str): The input string containing '0', '1', and '?'.

    Returns:
    str: The modified string with '?' replaced by '0' or '1' to minimize badness.
    """
    ones = S.count('1')
    zeroes = S.count('0')
    rand = S.count('?')
    diff = abs(ones - zeroes)
    added_ones = 0
    added_zeroes = 0
    
    if ones < zeroes:
        added_ones = diff
        rand -= diff
    else:
        added_zeroes = diff
        rand -= diff
    
    if rand > 0:
        added_zeroes += rand // 2
        added_ones += rand - rand // 2
    
    ans = ''
    for ele in S:
        if ele == '?':
            if added_ones > 0:
                ans += '1'
                added_ones -= 1
            else:
                ans += '0'
        else:
            ans += ele
    
    return ans