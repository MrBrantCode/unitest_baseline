"""
QUESTION:
CBI agents are investigating a case in which they came across certain names of the culprits. They decided to encode the names into the number format.
"Riya" is encoded as "729611390","Sumitha" as "73108101981109993" ,"Anandita" as "55101891039410011294" and so on. Given a String S denoting a name, Encode the name.
 
Example 1:
Input:
S = "Soni"
Output:
7310210298
Explanation:
The name when encoded gives the given Output.
Example 2:
Input:
S = " Pawan"
Output:
708811190104 
Explanation:
The name when encoded gives the given Output.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function encodeTheName() which takes a String S as input and returns a String as the encoded format.
 
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(|S|)
 
Constraints:
1 <= |S| <= 10^{4}
"""

def encode_name(s: str) -> str:
    encoded_string = ''
    for i in range(len(s)):
        encoded_string += str(ord(s[i]) - 10 + i)
    return encoded_string