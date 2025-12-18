"""
QUESTION:
An encoded string (s) is given, and the task is to decode it. The encoding pattern is that the occurrence of the string is given at the starting of the string and each string is enclosed by square brackets.
Note: The occurance of a single string is less than 1000.
Example 1:
Input: s = 1[b]
Output: b
Explaination: 'b' is present only one time.
Example 2:
Input: s = 3[b2[ca]]
Output: bcacabcacabcaca
Explaination: 2[ca] means 'ca' is repeated 
twice which is 'caca' which concatenated with 
'b' becomes 'bcaca'. This string repeated 
thrice becomes the output.
Your Task:
You do not need to read input or print anything. Your task is to complete the function decodedString() which takes s as the input parameter and returns the decoded string.
Expected Time Complexity: O(|s|)
Expected Auxiliary Space: O(|s|)
Constraints:
1 ≤ |s| ≤ 10^{3}
"""

def decode_string(s: str) -> str:
    st = []
    ans = ''
    for i in range(len(s)):
        if s[i] == ']':
            x = ''
            while st[-1] != '[':
                x = st.pop() + x
            st.pop()
            k = ''
            while st and st[-1].isdigit():
                k = st.pop() + k
            y = int(k) * x
            for i in y:
                st.append(i)
        else:
            st.append(s[i])
    while st:
        ans = st.pop() + ans
    return ans