"""
QUESTION:
You are given a string S. Every sub-string of identical letters is replaced by a single instance of that letter followed by the hexadecimal representation of the number of occurrences of that letter. Then, the string thus obtained is further encrypted by reversing it [ See the sample for more clarity ]. Print the Encrypted String.
Note: All Hexadecimal letters should be converted to Lowercase letters.
 
Example 1:
Input:
S = "aaaaaaaaaaa"
Output:
ba 
Explanation: 
aaaaaaaaaaa
Step1: a11 (a occurs 11 times)
Step2: a11 is ab [since 11 is b in
hexadecimal]
Step3: ba [After reversing]
Example 2:
Input:
S = "abc"
Output:
1c1b1a
Explanation: 
abc
Step1: a1b1c1
Step2: 1c1b1a [After reversing]
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function encryptString() which takes a String S and returns the answer.
 
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(1)
Constraints
1 <= |S| <= 10^{5}
"""

def encrypt_string(S: str) -> str:
    arr = list(S)
    ans = []
    char = arr[0]
    count = 1
    
    for i in range(1, len(arr) + 1):
        if i == len(arr):
            ans.append(char)
            ans.append(hex(count)[2:])
            break
        if arr[i] == char:
            count += 1
        else:
            ans.append(char)
            ans.append(hex(count)[2:])
            count = 1
            char = arr[i]
    
    ans = ans[::-1]
    encrypted_string = ''.join(ans)
    return encrypted_string