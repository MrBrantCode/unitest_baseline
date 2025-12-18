"""
QUESTION:
Given two fractions a/b and c/d, compare them and print the larger of the two.
Example 1:
Input:
s = "5/6, 11/45"
Output: 5/6
Explanation:
5/6=0.8333... and 11/45=0.2444.... 
Clearly, 5/6 is greater, so we output it.
 
Example 2:
Input:
s = "8/1, 8/1"
Output: equal
Explanation:
We can see that both the fractions are same, 
so they are equal.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function compareFrac() which takes the string s as input parameters and returns the fraction that is greater. If they are equal, then return "equal".
Expected Time Complexity: O(len|s|)
Expected Auxiliary Space: O(1)
 
Constraints:
0<=a,c<=1000
1<=b,d<=1000
"""

def compare_fractions(s: str) -> str:
    # Extract the first fraction
    a = ''
    for i in range(len(s)):
        if s[i] == '/':
            break
        else:
            a = a + s[i]
    
    b = ''
    for j in range(i + 1, len(s)):
        if s[j] == ',':
            break
        b = b + s[j]
    
    # Extract the second fraction
    c = ''
    for k in range(j + 2, len(s)):
        if s[k] == '/':
            break
        c = c + s[k]
    
    d = ''
    for l in range(k + 1, len(s)):
        d = d + s[l]
    
    # Convert to integers and compute the values
    m = int(a) / int(b)
    n = int(c) / int(d)
    
    # Compare the fractions
    if m > n:
        return f"{a}/{b}"
    elif m < n:
        return f"{c}/{d}"
    else:
        return 'equal'