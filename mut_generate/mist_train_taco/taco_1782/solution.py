"""
QUESTION:
Devu loves to play with binary strings a lot. One day he borrowed a binary string s of size n from his friend Churu. Before starting to play with it, he wants to make sure that string does not contain more than  k consecutive equal characters. For achieving that, only kind of operation he is allowed to perform is to flip any ith character of the string. 

As Devu is always in hurry to meet his girlfriend, he wants you to help him in finding out the minimum number of operations he will need. Also he wants you to print one of the possible modified string too.

-----Input-----
- First line of input contains an integer T denoting the number of test cases. 
- For each test case, there are two lines. 
- First line contains two space separated integers n, k as defined in the problem. 
- Next line contains string s of size n.

-----Output-----
- For each test case, print two lines.
- First line should contain an integer corresponding to minimum number of operations Devu needs.
- In second line, print one of the possible modified strings.

-----Constraints-----
Subtask #1: 20 points
- 1 ≤ T ≤ 100, 1 ≤ n ≤ 20, 1 ≤ k ≤ n

Subtask #2: 35 points
- 1 ≤ T ≤ 102, 1 ≤ n ≤ 103, 1 ≤ k ≤ n

Subtask #3: 45 points
- 1 ≤ T ≤ 105, 1 ≤ n ≤ 105, 1 ≤ k ≤ n
- Sum of n over all the test cases is ≤ 106 

-----Example-----
Input:
3
2 1
11
2 2
11
4 1
1001

Output:
1
10
0
11
2
1010

-----Explanation-----
Example case 1: As 1 is occurring twice consecutively, we can convert 11 to 10 in a single operation.
Example case 2: You don't need to modify the string as it does not have more than 2 equal consecutive character.
Example case 3: As 0 is occurring twice consecutively, we can convert 1001 to 1010 in a two operations (Flip third and fourth character).
"""

def minimize_consecutive_flips(s: str, k: int) -> (int, str):
    """
    Function to minimize the number of operations needed to ensure that the binary string s
    does not contain more than k consecutive equal characters by flipping any character.

    Parameters:
    - s (str): The binary string.
    - k (int): The maximum allowed consecutive equal characters.

    Returns:
    - (int, str): A tuple containing the minimum number of operations needed and one of the possible modified strings.
    """
    n = len(s)
    r = 0
    s = list(s)  # Convert string to list for mutability

    if k == 1:
        s0 = s[:]
        r0 = r1 = 0
        for (i, c) in enumerate(s):
            if i % 2:
                if c == '0':
                    s0[i] = '1'
                    r0 += 1
            elif c == '1':
                s0[i] = '0'
                r0 += 1
        s1 = s[:]
        for (i, c) in enumerate(s):
            if i % 2 == 0:
                if c == '0':
                    s1[i] = '1'
                    r1 += 1
            elif c == '1':
                s1[i] = '0'
                r1 += 1
        if r0 < r1:
            r = r0
            s = s0
        else:
            r = r1
            s = s1
    else:
        i = j = 0
        while j < n:
            while j < n and s[i] == s[j]:
                j += 1
            if j - i > k:
                for l in range(i + k, j, k + 1):
                    if l == j - 1:
                        l -= 1
                    s[l] = '0' if s[l] == '1' else '1'
                    r += 1
            i = j

    return r, ''.join(s)