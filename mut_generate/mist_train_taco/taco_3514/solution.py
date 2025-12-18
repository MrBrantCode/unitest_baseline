"""
QUESTION:
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter by a number of letters.  If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet.  In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

Example 

$s=\textbf{There's-a-star-waiting-in-the-sky}$ 

$k=3$  

The alphabet is rotated by $3$, matching the mapping above.  The encrypted string is $\textbf{Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb}$.  

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.  

Function Description  

Complete the caesarCipher function in the editor below.  

caesarCipher has the following parameter(s):

string s: cleartext  
int k: the alphabet rotation factor  

Returns  

string:  the encrypted string  

Input Format

The first line contains the integer, $n$, the length of the unencrypted string. 

The second line contains the unencrypted string, $\boldsymbol{\mathrm{~S~}}$. 

The third line contains $\boldsymbol{\mbox{k}}$, the number of letters to rotate the alphabet by.

Constraints

$1\leq n\leq100$ 

$0\leq k\leq100$ 

$\boldsymbol{\mathrm{~S~}}$ is a valid ASCII string without any spaces.   

Sample Input
11
middle-Outz
2

Sample Output
okffng-Qwvb

Explanation
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

m -> o
i -> k
d -> f
d -> f
l -> n
e -> g
-    -
O -> Q
u -> w
t -> v
z -> b
"""

def caesar_cipher(s: str, k: int) -> str:
    res = ''
    k = k % 26  # Normalize the shift to be within the range of 0-25
    
    for char in s:
        if char.isalpha():
            is_upper = char.isupper()
            ascii_new = ord(char) + k
            
            if is_upper and ascii_new > ord('Z'):
                ascii_new -= 26
            elif not is_upper and ascii_new > ord('z'):
                ascii_new -= 26
            
            res += chr(ascii_new)
        else:
            res += char
    
    return res