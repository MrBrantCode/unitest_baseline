"""
QUESTION:
Given a string S which consists of only lowercase English alphabets, you have to perform the below operations:
If the string S contains any repeating character, remove the first repeating character and reverse the string and again perform the above operation on the modified string, otherwise, you stop.
You have to find the final string.
Example 1:
Input: S = "abab"
Output: ba
Explanation:
In 1st operation: The first repeating 
character is a. After Removing the first 
character, S = "bab". After Reversing the 
string, S = "bab".
In 2nd operation: The first repeating 
character is b. After Removing the first 
character, S = "ab". After Reversing the 
string, S = "ba".
Now the string S does not contain any 
repeating character.
Example 2:
Input: S = "dddd"
Output: d
Explanation:
In 1st operation: The first repeating character 
is d. After Removing the first character, 
S = "ddd". After Reversing the string, S = "ddd". 
In 2nd operation: Similarly, S="dd".
In 3rd operation: Similarly, S="d".
Now the string S does not contain any repeating character.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function removeReverse( ) which accepts a string S input parameter and returns the modified string.
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(K), K <= 26.
Constraints:
The string contains only lowercase English alphabets.
1 < |S| < 10^{5}
|S| denotes the length of the string S.
"""

def remove_reverse(S: str) -> str:
    S = list(S)
    char_count = {}
    for char in S:
        char_count[char] = char_count.get(char, 0) + 1
    
    i, j = 0, len(S) - 1
    left_part, right_part = '', ''
    is_left_to_right = True
    operation_count = 0
    
    while i <= j:
        if is_left_to_right:
            if char_count[S[i]] > 1:
                char_count[S[i]] -= 1
                i += 1
                is_left_to_right = False
                operation_count += 1
            else:
                left_part += S[i]
                i += 1
        else:
            if char_count[S[j]] > 1:
                char_count[S[j]] -= 1
                j -= 1
                is_left_to_right = True
                operation_count += 1
            else:
                right_part = S[j] + right_part
                j -= 1
    
    final_string = left_part + right_part
    if operation_count % 2 == 1:
        final_string = final_string[::-1]
    
    return final_string