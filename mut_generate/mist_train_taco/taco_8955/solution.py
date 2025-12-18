"""
QUESTION:
Given a string S and array of strings, find whether the array contains a string with one character different from the given string.
 
Example 1:
Input :
N = 4
arr[] = {"bana","apple","banaba","bonanzo"}
S = "banana"
Output :
True
Explanation: 
banana and banaba has only one character 
different.
Example 2:
Input:
N = 4
arr[] = {"bana","apple","banaba","bonanzo"}
S = "apple"
Output :
False
Explanation: 
No string in arr differ by one 
character from S 
 
 Your Task:  
You don't need to read input or print anything. Your task is to complete the function isStringExist() which takes the string array arr[], its size N and a string S as input parameters and returns "True" if a string exists in arr which has only one character different from S else return "False".
 
Expected Time Complexity: O(N*Length of the string S)
Expected Space Complexity: O(1)
 
Constraints :
1 ≤ N ≤ 100
1 ≤| arr[i] | ≤ 1000
1 ≤| S | ≤ 1000
"""

def is_string_exist(arr, S):
    for item in arr:
        if len(item) == len(S):
            diff_count = 0
            for i in range(len(S)):
                if S[i] != item[i]:
                    diff_count += 1
                if diff_count > 1:
                    break
            if diff_count == 1:
                return True
    return False