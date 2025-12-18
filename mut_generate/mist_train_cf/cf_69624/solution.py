"""
QUESTION:
Function Name: decodeString

Description: Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times.

Restrictions: 
- The input string `s` is valid, with no extra white spaces, and well-formed square brackets.
- The original data does not contain any digits, and digits are only for those repeat numbers, `k`.
- The encoded string can contain nested encoded strings up to 3 levels deep.
- `1 <= s.length <= 100`
- `s` consists of lowercase English letters, digits, and square brackets '[]'.
- All the integers in `s` are in the range `[1, 300]`.
"""

def decodeString(s: str) -> str:
        
    nums = set(['0','1','2','3','4','5','6','7','8','9'])
    i,l = 0,len(s)
    
    def DFS(start):
            
        nonlocal s,nums
        stck, stk_num = [],[]
        mul = 0
        cpy_str = ''
            
        for i in range(start, len(s)):
            if s[i] in nums:
                mul = 10*mul + int(s[i])
                    
            elif s[i] == '[':
                stk_num.append(mul)
                mul = 0
                stck.append(cpy_str)
                cpy_str = ''
                    
            elif s[i] == ']':
                mul = stk_num.pop()
                cpy_str = mul*cpy_str
                cpy_str = stck.pop() + cpy_str
                mul = 0
                    
            else:cpy_str+=s[i]
                    
        return cpy_str
        
    return DFS(i)