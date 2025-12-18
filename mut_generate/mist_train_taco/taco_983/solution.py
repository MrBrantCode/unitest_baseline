"""
QUESTION:
You are given a string $s$, consisting of lowercase Latin letters. While there is at least one character in the string $s$ that is repeated at least twice, you perform the following operation:

you choose the index $i$ ($1 \le i \le |s|$) such that the character at position $i$ occurs at least two times in the string $s$, and delete the character at position $i$, that is, replace $s$ with $s_1 s_2 \ldots s_{i-1} s_{i+1} s_{i+2} \ldots s_n$.

For example, if $s=$"codeforces", then you can apply the following sequence of operations:

$i=6 \Rightarrow s=$"codefrces";

$i=1 \Rightarrow s=$"odefrces";

$i=7 \Rightarrow s=$"odefrcs";

Given a given string $s$, find the lexicographically maximum string that can be obtained after applying a certain sequence of operations after which all characters in the string become unique.

A string $a$ of length $n$ is lexicographically less than a string $b$ of length $m$, if:

there is an index $i$ ($1 \le i \le \min(n, m)$) such that the first $i-1$ characters of the strings $a$ and $b$ are the same, and the $i$-th character of the string $a$ is less than $i$-th character of string $b$;

or the first $\min(n, m)$ characters in the strings $a$ and $b$ are the same and $n < m$.

For example, the string $a=$"aezakmi" is lexicographically less than the string $b=$"aezus".


-----Input-----

The first line contains one integer $t$ ($1 \le t \le 10^4$). Then $t$ test cases follow.

Each test case is characterized by a string $s$, consisting of lowercase Latin letters ($1 \le |s| \le 2 \cdot 10^5$).

It is guaranteed that the sum of the lengths of the strings in all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

For each test case, output the lexicographically maximum string that can be obtained after applying a certain sequence of operations after which all characters in the string become unique.


-----Examples-----

Input
6
codeforces
aezakmi
abacaba
convexhull
swflldjgpaxs
myneeocktxpqjpz
Output
odfrces
ezakmi
cba
convexhul
wfldjgpaxs
myneocktxqjpz


-----Note-----

None
"""

def lexicographically_maximum_unique_string(s: str) -> str:
    cnt = [0] * 26  # Frequency count of each character
    vis = [0] * 26  # Visited status of each character
    
    # Count the frequency of each character in the string
    for char in s:
        cnt[ord(char) - ord('a')] += 1
    
    st = [30]  # Stack to keep track of characters in the desired order
    s_index = 0  # Index to keep track of the stack position
    
    for char in s:
        tmp = ord(char) - ord('a')
        if vis[tmp] == 0:
            # While the stack is not empty, the top of the stack is lexicographically smaller,
            # and the character at the top of the stack still has occurrences left, pop the stack
            while s_index and st[s_index] < tmp and cnt[st[s_index]] >= 1:
                vis[st[s_index]] = 0
                st.pop()
                s_index -= 1
            # Push the current character onto the stack
            st.append(tmp)
            s_index += 1
            vis[tmp] = 1
        cnt[tmp] -= 1
    
    # Construct the result string from the stack
    result = ''.join(chr(ord('a') + st[i]) for i in range(1, len(st)))
    return result