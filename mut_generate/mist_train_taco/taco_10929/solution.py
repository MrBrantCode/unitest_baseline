"""
QUESTION:
Read problems statements in Mandarin Chinese  and Russian. 
Once upon a time chef decided to learn encodings. And, obviously, he started with the easiest one (well, actually the easiest after Caesar cypher) – substitution cypher.

But very soon Chef got bored with encoding/decoding, so he started thinking how to hack this cypher. 
He already knows some algorithm, which is not always correct, 
but it’s sufficient for now. Here is its description.

Imagine we know frequency sequence of English letters (this means, that letters are sorted by their frequency of appearing in English texts, in ascending order). 
And let’s find frequency sequence of cyphered letters (if some of them appear equal number of times, then first in frequency sequence will be lower letter between them).
Now, using this two frequency sequences we can recover plain text. Just substitute cyphered letter with origin one, if they are at same positions in sequences. 

Now, Chef has frequency sequence of English letters and cypher text. And he asks you to recover plain text. Please, help him.

------ Input ------ 

In first line number T is given - number of test cases. Then T test cases follow. Each test case consists of two lines - frequency sequence and encrypted text.

------ Output ------ 

For each test case you should output decrypted with the given frequency sequence text. Please note, that the case of letters should be preserved. 

------ Constraints ------ 

$ 1 ≤ T ≤ 1000; $
$ Length of frequency sequence is always 26; $
$ 1 ≤ length of the text ≤ 150000; $
$ 1 ≤ sum lengths of all texts ≤ 150000. $
$ Frequency sequence consists of all lowercase English letters. Text consists of any characters. $

----- Sample Input 1 ------ 
3
qwrtyuipasdfgjkzxcvbnmheol
dummy!
bfgjklmopqrstuwxzhvnicdyea
abcd b efgd hbi!
qwrtyuipasdfgjkzxcvbnmheol
Dummy!
----- Sample Output 1 ------ 
hello!
have a nice day!
Hello!
"""

def decrypt_text(frequency_sequence, encrypted_text):
    # Create a list to store the frequency of each letter in the encrypted text
    arr = [[0, chr(i + 97)] for i in range(26)]
    
    # Count the frequency of each letter in the encrypted text
    for char in encrypted_text:
        char_lower = char.lower()
        if 'a' <= char_lower <= 'z':
            arr[ord(char_lower) - ord('a')][0] += 1
    
    # Sort the array based on frequency
    arr.sort()
    
    # Create a dictionary to map each letter in the frequency sequence to its corresponding letter in the encrypted text
    substitution_map = {}
    for i in range(26):
        substitution_map[arr[i][1]] = frequency_sequence[i]
    
    # Decrypt the text using the substitution map
    decrypted_text = ''
    for char in encrypted_text:
        if char.lower() in substitution_map:
            if char.islower():
                decrypted_text += substitution_map[char]
            else:
                decrypted_text += substitution_map[char.lower()].upper()
        else:
            decrypted_text += char
    
    return decrypted_text