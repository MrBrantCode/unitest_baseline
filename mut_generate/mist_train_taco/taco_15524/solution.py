"""
QUESTION:
You're given a string S of length N and an integer K. 
 
Let C denote the set of all characters in S. The string S is called *good* if, for every *suffix* of S:
The difference between the frequencies of any two characters in C does not exceed K.  
In particular, if the set C has a single element, the string S is *good*.

Find whether there exists a rearrangement of S which is *good*.  
If multiple such rearrangements exist, print the lexicographically smallest rearrangement.  
If no such rearrangement exists, print -1 instead.

Note that a suffix of a string is obtained by deleting some (possibly zero) characters from the beginning of the string. For example, the suffixes of S = abca are \{a, ca, bca, abca\}.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of two lines of input.
- The first line of each test case contains two space-separated integers N and K — the length of the string and the positive integer as mentioned in the statement, respectively.
- The next line consists of a string S of length N containing lowercase English alphabets only.

------ Output Format ------ 

For each test case, output on a new line the lexicographically smallest *good* rearrangement of S.

If no such rearrangement exists, print -1 instead.

------ Constraints ------ 

$1 ≤ T ≤ 2000$
$1 ≤ N ≤ 10^{5}$
$1 ≤ K ≤ N$
$S$ consists of lowercase english alphabets only.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^{5}$.

----- Sample Input 1 ------ 
4
3 1
aaa
4 2
baba
4 1
babb
7 2
abcbcac

----- Sample Output 1 ------ 
aaa
aabb
-1
abcabcc

----- explanation 1 ------ 
Test case $1$: Since $C = \{a\}$, the string $S$ is *good*.

Test case $2$: The set $C = \{a, b\}$. Consider the rearrangement $aabb$. Let $f_{a}$ and $f_{b}$ denote the frequencies of $a$ and $b$ respectively:
- In suffix $b$, $f_{b} = 1$ and $f_{a} = 0$. Thus, $|f_{b}-f_{a}| = 1 ≤ K$.
- In suffix $bb$, $f_{b} = 2$ and $f_{a} = 0$. Thus, $|f_{b}-f_{a}| = 2 ≤ K$.
- In suffix $abb$, $f_{b} = 2$ and $f_{a} = 1$. Thus, $|f_{b}-f_{a}| = 1 ≤ K$.
- In suffix $aabb$, $f_{b} = 2$ and $f_{a} = 2$. Thus, $|f_{b}-f_{a}| = 0 ≤ K$.

Thus, the rearrangement $aabb$ is good. It is also the lexicographically smallest rearrangement possible of string $S$.

Test case $3$: It can be proven that there exists no rearrangement of $S$ which is *good*.

Test case $4$: The set $C = \{a, b, c\}$. Consider the rearrangement $abcabcc$. Let $f_{a}, f_{b},$ and $f_{c}$ denote the frequencies of $a, b,$ and $c$ respectively:
- In suffix $c$, $f_{a} = 0, f_{b} = 0, $ and $f_{c} = 1$. Thus, $|f_{b}-f_{a}|, |f_{c}-f_{b}|,$ and $|f_{a}-f_{c}|$ are all less than or equal to $K = 2$.
- In suffix $cc$, $f_{a} = 0, f_{b} = 0, $ and $f_{c} = 2$. Thus, $|f_{b}-f_{a}|, |f_{c}-f_{b}|,$ and $|f_{a}-f_{c}|$ are all less than or equal to $K = 2$.
- In suffix $bcc$, $f_{a} = 0, f_{b} = 1, $ and $f_{c} = 2$. Thus, $|f_{b}-f_{a}|, |f_{c}-f_{b}|,$ and $|f_{a}-f_{c}|$ are all less than or equal to $K = 2$.
- In suffix $abcc$, $f_{a} = 1, f_{b} = 1, $ and $f_{c} = 2$. Thus, $|f_{b}-f_{a}|, |f_{c}-f_{b}|,$ and $|f_{a}-f_{c}|$ are all less than or equal to $K = 2$.
- In suffix $cabcc$, $f_{a} = 1, f_{b} = 1, $ and $f_{c} = 3$. Thus, $|f_{b}-f_{a}|, |f_{c}-f_{b}|,$ and $|f_{a}-f_{c}|$ are all less than or equal to $K = 2$.
- In suffix $bcabcc$, $f_{a} = 1, f_{b} = 2, $ and $f_{c} = 3$. Thus, $|f_{b}-f_{a}|, |f_{c}-f_{b}|,$ and $|f_{a}-f_{c}|$ are all less than or equal to $K = 2$.
- In suffix $abcabcc$, $f_{a} = 2, f_{b} = 2, $ and $f_{c} = 3$. Thus, $|f_{b}-f_{a}|, |f_{c}-f_{b}|,$ and $|f_{a}-f_{c}|$ are all less than or equal to $K = 2$.

Thus, the rearrangement $abcabcc$ is good. It is also the lexicographically smallest *good* rearrangement of string $S$.
"""

def find_lexicographically_smallest_good_rearrangement(S, K):
    from collections import Counter
    
    # Count the frequency of each character in the string
    char_count = Counter(S)
    
    # Get the list of character frequencies
    frequencies = list(char_count.values())
    
    # Check if the maximum frequency difference is within the allowed limit K
    if max(frequencies) - min(frequencies) > K:
        return -1
    
    # Initialize the result string
    result = ''
    flag = False
    
    # While there are characters left to process
    while len(result) < len(S):
        while not flag and char_count:
            # Sort the keys (characters) lexicographically
            keys = sorted(char_count.keys())
            if char_count[keys[-1]] <= K:
                # Append the character repeated by its count to the result
                result = keys[-1] * char_count[keys[-1]] + result
                del char_count[keys[-1]]
            else:
                # Append the character repeated by (K - 1) times to the result
                result = keys[-1] * (K - 1) + result
                char_count[keys[-1]] -= (K - 1)
                flag = True
        
        while flag and char_count:
            # Sort the remaining characters lexicographically and append them to the result
            keys = sorted(char_count.keys())
            result = ''.join(keys) + result
            # Decrease the count of each character by 1 and remove characters with zero count
            to_remove = []
            for key in char_count:
                char_count[key] -= 1
                if char_count[key] == 0:
                    to_remove.append(key)
            if char_count[keys[-1]] < 2:
                flag = False
            for key in to_remove:
                del char_count[key]
    
    return result