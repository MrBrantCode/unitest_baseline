"""
QUESTION:
One of the simple ciphers is the affine cipher. First, replace the letters a to z with the numbers a = 0, b = 1, c = 2, ..., x = 23, y = 24, z = 25 and 0 to 25. Then replace the original alphabet with the following formula.

$ F (\ gamma) = (\ alpha \ cdot \ gamma + \ beta) $ mod $ 26 $

However, mod 26 represents the remainder after dividing by 26. For example, when $ \ alpha = 3, \ beta = 2 $, the alphabet'a'(= 0) is $ F (0) = (3 \ cdot 0 + 2) $ mod $ 26 = 2 $ and'c In', the alphabet'n'(= 13) is replaced with'p' at $ F (13) = (3 \ cdot 13 + 2) $ mod $ 26 = 15 $. At this time, it is assumed that $ \ alpha $ and $ \ beta $ are carefully selected so that $ F (\ gamma) $ is always associated with $ \ gamma $ on a one-to-one basis ($ \ alpha). As long as $ and 26 are relatively prime). $ F ('a') = 7, F ('n') = 7 $, as in $ \ alpha = 4, \ beta = 7 $, and'a'and'n' are the same'h' It will not be replaced by. Also, non-alphabetic characters are not replaced.

Create a program that outputs the encrypted character string decrypted into the original text. In the original text, as a keyword


that
this


It is assumed that one of the above is always included.



Input

Given multiple datasets. The first line gives the number of datasets $ n $ ($ n \ leq 30 $). It is followed by $ n $ rows of data. Each dataset is given an encrypted sentence of up to 256 characters consisting of lowercase letters and blanks on one line.

Output

For each dataset, output the decrypted original text on one line.

Example

Input

1
y eazqyp pnop pngtg ye obmpngt xmybp mr lygw


Output

i submit that there is another point of view
"""

def affine_cipher_decrypt(encrypted_text, keywords=['that', 'this']):
    z = 'abcdefghijklmnopqrstuvwxyz'
    
    for i in range(1, 26, 2):
        for j in range(26):
            decrypted_text = ''
            for c in encrypted_text:
                if c in z:
                    decrypted_text += z[(z.index(c) * i + j) % 26]
                else:
                    decrypted_text += c
            
            for keyword in keywords:
                if keyword in decrypted_text:
                    return decrypted_text
    
    return None