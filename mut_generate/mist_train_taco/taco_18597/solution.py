"""
QUESTION:
Solve the mystery.  
Input:
String which consists of words(all the characters of any word are lower case letters) and punctuation marks(consists of {'.' , ',' , '?' , '!'}). Also every input string consists of one '*' in it.
It is guaranteed that strings doesn't start or end with space(' ') and only one answer exists for each case.  

Output:
Lower case letter.  

Constrains:
1 ≤ t ≤ 1000
2 ≤ length of string(n) ≤ 100  

Problem Setter : Vinay Kumar

SAMPLE INPUT
7
k! cats s*ack.
ah, s*tan sees natasha!
aibohphobi*
al lets della call ed ste*la.
amy, must i jujitsu *y ma?
aerata pat a*ea.
lollipop i * lol.

SAMPLE OUTPUT
t
a
a
l
m
r
l
"""

def find_mystery_letter(input_string: str) -> str:
    # Initialize an empty string to store the alphanumeric characters and '*'
    st = ""
    
    # Iterate through each character in the input string
    for char in input_string:
        # Append alphanumeric characters and '*' to the string 'st'
        if char.isalnum() or char == '*':
            st += char
    
    # Calculate the length of the string 'st'
    le = len(st)
    
    # Iterate through the first half of the string 'st'
    for i in range(le // 2):
        # Check if the current character or its mirror character is '*'
        if st[i] == '*' or st[le - 1 - i] == '*':
            # Return the non-'*' character
            if st[i] == '*':
                return st[le - 1 - i]
            else:
                return st[i]

    # If no '*' is found (which shouldn't happen due to problem constraints), return an empty string
    return ""