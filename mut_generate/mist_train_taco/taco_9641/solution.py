"""
QUESTION:
Chef has two strings A and B of lengths N and M respectively.

Chef can rearrange both strings in any way he wants. Let the rearranged string of A be A' and the rearranged string of B be B'. 

Determine whether we can construct rearrangements A' and B' such that (A' + B') is a palindrome.

Here + denotes the concatenation operation. For e.g. {abc} + {xyz} = {abcxyz}.

Note: A string is called palindrome if it reads the same backwards and forwards, for e.g. \texttt{noon} and \texttt{level} are palindromic strings.

------ Input Format ------ 

- The first line contains a single integer T — the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers N and M — the length of the strings A and B respectively.
- The second line of each test case contains a string A of length N containing lowercase Latin letters only.
- The third line of each test case contains a string B of length M containing lowercase Latin letters only.

------ Output Format ------ 

For each test case, output YES if we can rearrange A and B such that (A' + B') becomes a palindrome. Otherwise, output NO.

You may print each character of YES and NO in uppercase or lowercase (for example, yes, yEs, Yes will be considered identical).

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N, M ≤ 2 \cdot 10^{5}$
$A$ and $B$ consist of lowercase Latin letters only.
- The sum of $N + M$ over all test cases does not exceed $2 \cdot 10^{5}$.

----- Sample Input 1 ------ 
4
5 2
abcdd
ac
3 3
abc
xyz
2 4
aa
aaaa
1 3
a
aax

----- Sample Output 1 ------ 
YES
NO
YES
NO

----- explanation 1 ------ 
Test case $1$: We can rearrange $A$ to $A' = acdbd$ and $B$ to $B' = ca$. So $A' + B' = acdbdca$ which is palindromic.

Test case $2$: We can not rearrange $A$ and $B$ such that $A' + B'$ is palindromic.

Test case $3$: For $A' = aa$ and $B' = aaaa$, $A' + B' = aaaaaa$ is palindromic.
"""

from collections import Counter

def can_form_palindrome(A, B, N, M):
    # Concatenate the strings
    combined = A + B
    
    # Count the frequency of each character in the combined string
    char_count = Counter(combined)
    
    # Count the number of characters with odd frequencies
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    
    # If more than one character has an odd frequency, it's not possible to form a palindrome
    if odd_count > 1:
        return 'NO'
    
    # If N > M, swap A and B to ensure A is the shorter string
    if N > M:
        A, B = B, A
    
    # Check if all characters in B can be matched with characters in A
    A_count = Counter(A)
    for char in B:
        if A_count[char] == 0:
            return 'NO'
        A_count[char] -= 1
    
    return 'YES'