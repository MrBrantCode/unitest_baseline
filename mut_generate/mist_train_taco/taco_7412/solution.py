"""
QUESTION:
Return the largest possible k such that there exists a_1, a_2, ..., a_k such that:

Each a_i is a non-empty string;
Their concatenation a_1 + a_2 + ... + a_k is equal to text;
For all 1 <= i <= k,  a_i = a_{k+1 - i}.

 
Example 1:
Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".

Example 2:
Input: text = "merchant"
Output: 1
Explanation: We can split the string on "(merchant)".

Example 3:
Input: text = "antaprezatepzapreanta"
Output: 11
Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".

Example 4:
Input: text = "aaa"
Output: 3
Explanation: We can split the string on "(a)(a)(a)".

 
Constraints:

text consists only of lowercase English characters.
1 <= text.length <= 1000
"""

def longest_decomposition(text: str) -> int:
    n = len(text)
    splits = 0
    leftstart, leftend = 0, 0
    rightstart, rightend = n - 1, n - 1
    
    while leftend < rightstart:
        if text[leftstart:leftend + 1] == text[rightstart:rightend + 1]:
            leftstart = leftend + 1
            leftend = leftstart
            rightstart = rightstart - 1
            rightend = rightstart
            splits += 2
        else:
            leftend += 1
            rightstart -= 1
    
    return splits + 1 if leftstart <= rightend else splits