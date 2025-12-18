"""
QUESTION:
You are given a string s of lower case english alphabets. You can choose any two characters in the string and replace all the occurences of the first character with the second character and replace all the occurences of the second character with the first character. Your aim is to find the lexicographically smallest string that can be obtained by doing this operation at most once.
Example 1:
Input:
A = "ccad"
Output: "aacd"
Explanation:
In ccad, we choose a and c and after 
doing the replacement operation once we get, 
aacd and this is the lexicographically
smallest string possible. 
 
Example 2:
Input:
A = "abba"
Output: "abba"
Explanation:
In abba, we can get baab after doing the 
replacement operation once for a and b 
but that is not lexicographically smaller 
than abba. So, the answer is abba. 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function chooseandswap() which takes the string A as input parameters and returns the lexicographically smallest string that is possible after doing the operation at most once.
Expected Time Complexity: O(|A|) length of the string A
Expected Auxiliary Space: O(1)
 
Constraints:
1<= |A| <=10^{5}
"""

def lexicographically_smallest_string(s: str) -> str:
    arr = list(s)
    freq = [0] * 26
    
    # Calculate frequency of each character
    for c in arr:
        freq[ord(c) - ord('a')] += 1
    
    # Try to find the lexicographically smallest string
    for i in range(len(arr)):
        curr = arr[i]
        for j in range(ord(curr) - ord('a')):
            if freq[j] > 0:
                return replace(arr, curr, chr(ord('a') + j))
        freq[ord(curr) - ord('a')] = 0
    
    return s

def replace(arr: list, a: str, b: str) -> str:
    for i in range(len(arr)):
        if arr[i] == a:
            arr[i] = b
        elif arr[i] == b:
            arr[i] = a
    return ''.join(arr)