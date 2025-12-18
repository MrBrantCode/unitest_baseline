"""
QUESTION:
Given an array of strings arr[] of size N, find if there exists 2 strings arr[i] and arr[j] such that arr[i]+arr[j] is a palindrome i.e the concatenation of string arr[i] and arr[j] results into a palindrome.
Example 1:
Input:
N = 6
arr[] = {"geekf", "geeks", "or","keeg", "abc", 
          "bc"}
Output: 1 
Explanation: There is a pair "geekf"
and "keeg".
Example 2:
Input:
N = 5
arr[] = {"abc", "xyxcba", "geekst", "or", "bc"}
Output: 1
Explanation: There is a pair "abc"
and "xyxcba".
Your Task:  
You don't need to read input or print anything. Your task is to complete the function palindromepair() which takes the array arr[], its size N and returns true if palindrome pair exists and returns false otherwise.
The driver code itself prints 1 if returned value is true and prints 0 if returned value is false.
 
Expected Time Complexity: O(N*l^{2}) where l = length of longest string in arr[]
Expected Auxiliary Space: O(N*l^{2}) where l = length of longest string in arr[]
 
Constraints:
1 ≤ N ≤ 2*10^{4}
1 ≤ |arr[i]| ≤ 10
"""

def is_palindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def has_palindrome_pair(arr, n):
    mp = {}
    for i in range(n):
        s = arr[i]
        s_reversed = s[::-1]
        mp[s_reversed] = i
    
    for i in range(n):
        for j in range(len(arr[i])):
            s1 = arr[i][:j]
            s2 = arr[i][j:]
            if s1 in mp and is_palindrome(s2) and (mp[s1] != i):
                return True
            if s2 in mp and is_palindrome(s1) and (mp[s2] != i):
                return True
    
    return False