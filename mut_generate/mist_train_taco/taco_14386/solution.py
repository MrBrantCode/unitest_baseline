"""
QUESTION:
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string $\mbox{S}$. Suppose a character '$\textbf{C}$' occurs consecutively $\mbox{X}$ times in the string. Replace these consecutive occurrences of the character '$\textbf{C}$' with $(X,c)$ in the string. 

For a better understanding of the problem, check the explanation. 

Input Format

A single line of input consisting of the string $\mbox{S}$. 

Output Format 

A single line of output consisting of the modified string.

Constraints

All the characters of $\mbox{S}$ denote integers between $\mbox{o}$ and $\mbox{9}$. 

$1\leq\big|\text{}S\big|\leq10^4$

Sample Input

1222311

Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)

Explanation

First, the character $\mbox{I}$ occurs only once. It is replaced by $(1,\:\:1)$. Then the character $2$ occurs three times, and it is replaced by $(3,2)$ and so on. 

Also, note the single space within each compression and between the compressions.
"""

def compress_string(s: str) -> str:
    if not s:
        return ""
    
    result = []
    act = s[0]
    num = 1
    
    for i in range(1, len(s)):
        if s[i] == act:
            num += 1
        else:
            result.append(f"({num}, {act})")
            act = s[i]
            num = 1
    
    # Append the last group
    result.append(f"({num}, {act})")
    
    return ' '.join(result)