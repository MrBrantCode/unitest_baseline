"""
QUESTION:
Takahashi wants to be a member of some web service.
He tried to register himself with the ID S, which turned out to be already used by another user.
Thus, he decides to register using a string obtained by appending one character at the end of S as his ID.
He is now trying to register with the ID T. Determine whether this string satisfies the property above.

-----Constraints-----
 - S and T are strings consisting of lowercase English letters.
 - 1 \leq |S| \leq 10
 - |T| = |S| + 1

-----Input-----
Input is given from Standard Input in the following format:
S
T

-----Output-----
If T satisfies the property in Problem Statement, print Yes; otherwise, print No.

-----Sample Input-----
chokudai
chokudaiz

-----Sample Output-----
Yes

chokudaiz can be obtained by appending z at the end of chokudai.
"""

def is_valid_appended_id(S: str, T: str) -> str:
    # Check if T is exactly one character longer than S
    if len(T) != len(S) + 1:
        return "No"
    
    # Check if T can be obtained by appending one character to S
    if S == T[:-1]:
        return "Yes"
    else:
        return "No"