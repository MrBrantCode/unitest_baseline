"""
QUESTION:
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string $\boldsymbol{\mathrm{~S~}}$, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.  
If the occurrence count is the same, sort the characters in alphabetical order.   

For example, according to the conditions described above, 

$\textbf{G00GLE}$ would have it's logo with the letters $\textbf{G},\textbf{C},\textbf{E}$. 

Input Format

A single line of input containing the string $\mbox{S}$.  

Constraints

$3<len(S)\leq10^4$   
$\mbox{S}$ has at least $3$ distinct characters   

Output Format

Print the three most common characters along with their occurrence count each on a separate line. 

Sort output in descending order of occurrence count. 

If the occurrence count is the same, sort the characters in alphabetical order.  

Sample Input 0
aabbbccde

Sample Output 0
b 3
a 2
c 2

Explanation 0

$\textsf{aabbccde}$

Here, b occurs $3$ times. It is printed first.

Both a and c occur $2$ times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string $\mbox{S}$ has at least $3$ distinct characters.
"""

from collections import Counter

def get_top_three_characters(S: str) -> list:
    # Count the occurrences of each character
    counts = Counter(S).most_common()
    
    # Sort by occurrence count (descending) and then by character (ascending)
    counts.sort(key=lambda x: (-x[1], x[0]))
    
    # Return the top three characters
    return counts[:3]