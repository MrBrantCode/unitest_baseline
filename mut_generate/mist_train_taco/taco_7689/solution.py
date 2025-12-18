"""
QUESTION:
Problem A: Swap crypto

A 2D enthusiast at R University, he often writes embarrassing sentences that blush when seen by people. Therefore, in order for a third party to not be able to see the text he is writing, he encrypts the text using a method called swap encryption that he devised independently. In swap encryption, the following steps are repeated N times to perform encryption.

1. Swap the ai and bi of the string
2. Return these two characters in alphabetical order by the difference between ai and bi



However, in alphabetical order, "z" is used before "a".

For example, if the character string "aojwo" is encrypted with a1 = 1 and b1 = 4, it will be as follows.

1. Swap the 1st and 4th ("aojwo" → "wojao")
2. Return these two letters'w'and'a' in alphabetical order by the difference between 1 and 4 = 3 ("wojao"-> "tojxo")
* If'w'is returned by 3 in alphabetical order, it becomes'w' →'v' →'u' →'t'.
* If'a'is returned by 3 in alphabetical order, it becomes'a' →'z' →'y' →'x'.



Therefore, "aojwo" is encrypted as "tojxo".

This encryption should have allowed him to encrypt his text without knowing the original text, but perhaps he leaked the swap operation process he used to encrypt it. Your job is to create a program that "decrypts" given the encrypted strings and the swap operation used for encryption, and dismisses him as a 2D enthusiast.

Input

The input consists of multiple datasets. The total number of datasets is 20 or less. Each dataset has the following format:


N
message
a1 b1
...
ai bi
...
aN bN


N (0 <N ≤ 100) is an integer that indicates the number of swap operations when encrypting. message indicates encrypted data. Cryptographic data is a character string consisting of only lowercase letters of the alphabet. If the length of the message is len, we can assume that 2 ≤ len ≤ 100.

ai and bi represent two indexes that have been swapped in encryption. You can assume that 1 ≤ ai <bi ≤ len. For encryption, it is assumed that the swap operations are performed in the order in which they are entered.

The end of the input is indicated by a single line consisting of only 0s. This data does not need to be processed.

Output

Output the decrypted string on one line for each dataset.

Sample Input


1
tojxo
14
Five
uhcqmlmkv
4 5
6 9
3 6
1 7
3 6
Five
shzxadexonr
8 9
3 9
5 8
4 9
10 11
0



Output for Sample Input


aojwo
shinryaku
shitadegeso






Example

Input

1
tojxo
1 4
5
uhcqmlmkv
4 5
6 9
3 6
1 7
3 6
5
shzxadexonr
8 9
3 9
5 8
4 9
10 11
0


Output

aojwo
shinryaku
shitadegeso
"""

def decrypt_message(n, message, ablst):
    # Convert the message to a list of integers representing characters
    mes = [ord(c) - ord('a') for c in message]
    
    # Reverse the list of swap operations
    ablst.reverse()
    
    # Perform the decryption operations
    for (a, b) in ablst:
        a -= 1
        b -= 1
        (mes[b], mes[a]) = ((mes[a] + (b - a)) % 26, (mes[b] + (b - a)) % 26)
    
    # Convert the list of integers back to characters
    mes = [chr(i + ord('a')) for i in mes]
    
    # Join the list into a single string and return
    return ''.join(mes)