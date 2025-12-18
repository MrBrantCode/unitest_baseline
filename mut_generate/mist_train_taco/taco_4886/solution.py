"""
QUESTION:
### Background
In classical cryptography, the Hill cipher is a polygraphic substitution cipher based on linear algebra. It was invented by Lester S. Hill in 1929.



### Task


This cipher involves a text key which has to be turned into a matrix and text which needs to be encoded. The text key can be of any perfect square length but for the sake of this kata we will focus on keys of length 4 forming a 2x2 matrix.

To encrypt a message using the hill cipher, first of all you need to convert the text key into a key matrix. To do that you will convert the key row wise into a 2x2 matrix. Then you will substitute the letters with their respective positions on the alphabet: A=0, B=1,C=2 and so on till Z=25. So for example if we get the key text as ```cats```, the key matrix will be:
    
    [[ 2  0]
     [19 18]]
     
Now the next step is to break the text into pairs of two and convert those pairs into 2x1 matrices. If your text has an odd number of letters then just add a Z next to your last letter. Now again convert those letters into their respective position in the alphabet as above. So for example the text ```Hi``` would be converted into:

    [[7]
     [8]]
     
Now we need to [multiply](https://www.mathsisfun.com/algebra/matrix-multiplying.html) the key matrix by the text matrix to get our encrypted matrix and then find out the encrypted matrix [modulo](https://en.wikipedia.org/wiki/Modulo_operation) 26:

    [[ 2  0]  *  [[7]  =  [[14]   =  [[14]  mod 26
     [19 18]]     [8]]     [277]]     [17]]
     
For the final step we just find out the letters at the alphabet position of 14 and 17 which are ```O``` and ```R```. So ```OR``` is our encrypted message for the message ```Hi```


In this kata you will be given a function named ```encrypt``` with the parameters ```text``` and ```key``` and you have to return the encrypted message in all uppercase letters

``` python
encrypt('','azyb') → ''
encrypt('Hi','cats') → 'OR'
encrypt('This is a good day','bbaa') → 'AAAAAAGACAGAYA'
```

Note:
- The text to encrypt will contain characters other than the alphabets, its your job to clean them before converting text to matrices. Spaces also need to be removed
- The text may contain both uppercase and lowercase alphabets. Its your job to standardize them, the encrypted text however should be returned in uppercase letters.
- The key will always contain 4 lowercase alphabet.
"""

import numpy as np
from itertools import zip_longest
from string import ascii_lowercase as lower, ascii_uppercase as upper

# Dictionary to map characters to their respective positions in the alphabet
D = {c: i % 26 for (i, c) in enumerate(lower + upper)}

def hill_cipher_encrypt(text, key):
    # Initialize the result list to store the encrypted characters
    result = []
    
    # Clean the text by removing non-alphabetic characters and converting to lowercase
    text = ''.join(filter(str.isalpha, text)).lower()
    
    # Convert the key into a 2x2 matrix using the dictionary D
    key_matrix = np.array([[D[key[0]], D[key[1]]], [D[key[2]], D[key[3]]]])
    
    # Process the text in pairs, filling the last pair with 'Z' if necessary
    for c1, c2 in zip_longest(text[::2], text[1::2], fillvalue='z'):
        # Convert the pair into a 2x1 matrix
        text_matrix = np.array([[D[c1]], [D[c2]]])
        
        # Multiply the key matrix by the text matrix and take modulo 26
        encrypted_matrix = key_matrix @ text_matrix % 26
        
        # Convert the resulting matrix back to characters and append to result
        result.append(upper[encrypted_matrix[0, 0]] + upper[encrypted_matrix[1, 0]])
    
    # Join the result list into a single string and return
    return ''.join(result)