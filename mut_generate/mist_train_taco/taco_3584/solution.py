"""
QUESTION:
Utkarsh has recently started taking English-language classes to improve his reading and writing skills. However, he is still struggling to learn English. His teacher gave him the following problem to improve his vowel-identification skills:

There is a string S of length N consisting of lowercase English letters only. Utkarsh has to start from the first letter of the string.  
Each time he encounters a vowel (i.e. a character from the set \{a, e, i, o, u\}) he has to reverse the entire substring that came before the vowel. 

Utkarsh needs help verifying his answer. Can you print the final string after performing all the operations for him? 

------ Input Format ------ 

- First line will contain T, number of test cases. Then T test cases follow.
- The first line of each test case contains N, the length of the string.
- The second line contains S, the string itself.

------ Output Format ------ 

For each test case, output in a single line the final string after traversing S from left to right and performing the necessary reversals.

------ Constraints ------ 

$1 ≤ T ≤ 10^{4}$
$1 ≤ N ≤ 10^{6}$
- Sum of $N$ over all test cases does not exceed $10^{6}$.

----- Sample Input 1 ------ 
2
10
abcdefghij
7
bcadage
----- Sample Output 1 ------ 
hgfeabcdij
gacbade
----- explanation 1 ------ 
Test case $1$: The first letter is a vowel, but there is no substring before it to reverse, so we leave it as it is. Next, we reverse abcd and the string becomes dcbaefghij. Next we reach the vowel i and reverse dcbaefgh to get the string hgfeabcdij.

Test case $2$: Initially, we reverse bc and the string becomes cbadage. Next we reach the vowel a and reverse cbad to get the string dabcage. Finally we reach the vowel e and reverse dabcag to get the string gacbade.
"""

from collections import deque

def process_string_with_vowel_reversals(S: str, N: int) -> str:
    pi = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    p = deque()
    flag = 0
    
    for i in range(N):
        if S[i] in pi:
            flag = abs(flag - 1)
            if flag == 0:
                p.appendleft(S[i])
            else:
                p.append(S[i])
        elif flag == 0:
            p.appendleft(S[i])
        else:
            p.append(S[i])
    
    final_string = ''
    if flag == 0:
        while p:
            final_string += p.pop()
    else:
        while p:
            final_string += p.popleft()
    
    return final_string