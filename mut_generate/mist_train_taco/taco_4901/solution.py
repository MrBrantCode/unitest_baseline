"""
QUESTION:
Shaka and his brother have created a boring game which is played like this:  

They take a word composed of lowercase English letters and try to get the maximum possible score by building exactly 2 palindromic subsequences. The score obtained is the product of the length of these 2 subsequences.

Let's say $\mbox{A}$ and $\mbox{B}$ are two subsequences from the initial string. If $A_i$ & $A_j$ are the smallest and the largest positions (from the initial word) respectively in $\mbox{A}$ ; and $B_i$ & $B_j$ are the smallest and the largest positions (from the initial word) respectively in $\mbox{B}$, then the following statements hold true: 

$A_i\leq A_j$, 

$B_i\leq B_j$, & 

$A_j<B_i$. 

i.e., the positions of the subsequences should not cross over each other. 

Hence the score obtained is the product of lengths of subsequences $\mbox{A}$ & $\mbox{B}$. Such subsequences can be numerous for a larger initial word, and hence it becomes harder to find out the maximum possible score. Can you help Shaka and his brother find this out?

Input Format

Input contains a word $\mbox{S}$ composed of lowercase English letters in a single line.  

Constraints

$1<|S|\leq3000$ 

each character will be a lower case english alphabet.  

Output Format

Output the maximum score the boys can get from $\mbox{S}$.

Sample Input
eeegeeksforskeeggeeks

Sample Output
50

Explanation

A possible optimal solution is eee-g-ee-ksfor-skeeggeeks being eeeee the one subsequence and skeeggeeks the other one. We can also select eegee in place of eeeee, as both have the same length.
"""

def max_palindromic_subsequences_score(s: str) -> int:
    length = len(s)
    seq_length = [[0 for _ in range(length)] for _ in range(length)]
    
    # Initialize the diagonal with 1s because each single character is a palindrome of length 1
    for i in range(length):
        seq_length[i][i] = 1
    
    # Fill the seq_length matrix
    for cols in range(2, length + 1):
        for i in range(0, length - cols + 1):
            j = i + cols - 1
            if s[i] == s[j]:
                if cols == 2:
                    seq_length[i][j] = 2
                else:
                    seq_length[i][j] = seq_length[i + 1][j - 1] + 2
            else:
                seq_length[i][j] = max(seq_length[i + 1][j], seq_length[i][j - 1])
    
    # Calculate the maximum score
    max_score = 0
    for i in range(0, length - 1):
        left = seq_length[0][i]
        right = seq_length[i + 1][-1]
        score = left * right
        if score > max_score:
            max_score = score
    
    return max_score