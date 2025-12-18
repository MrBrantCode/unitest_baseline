"""
QUESTION:
Everyone Knows AdFly and their Sister Sites.

If we see the Page Source of an ad.fly site we can see this perticular line:
Believe it or not This is actually the Encoded url which you would skip to.

The Algorithm is as Follows:
```
1) The ysmm value is broken like this

ysmm   = 0 1 2 3 4 5 6 7 8 9  = "0123456789"
code1  = 0   2   4   6   8    = "02468"
code2  =   9   7   5   3   1  = "97531"

2) code1+code2 is base64 Decoded

3) The result will be of this form :
https://adf.ly/go.php?u=

4)  has to be further decoded and the result is to be returned
```

Your Task:

```
Make a function to Encode text to ysmm value.

and a function to Decode ysmm value.
```

Note: Take random values for The first 2 int values.
I personally hate trivial error checking like giving integer input in place of string. 

```
Input For Decoder & Encoder: Strings
Return "Invalid" for invalid Strings
```
"""

import base64
import binascii
import math
from itertools import zip_longest

def decode_ysmm(ysmm):
    code1 = ''
    code2 = ''
    flip = False
    for c in ysmm:
        if flip:
            code2 += c
        else:
            code1 += c
        flip = not flip
    try:
        url = base64.b64decode(code1 + code2[len(code2)::-1])
    except binascii.Error:
        return 'Invalid'
    try:
        dec = base64.b64decode(url[26:])
    except binascii.Error:
        return 'Invalid'
    return str(dec, 'utf-8')

def encode_ysmm(url):
    prefix = '96https://adf.ly/go.php?u='
    full = str.encode(prefix) + base64.b64encode(str.encode(url))
    enc = base64.b64encode(full)
    cut = math.ceil(len(enc) / 2)
    code1 = str(enc[:cut + 1], 'utf-8')
    code2 = str(enc[len(enc):cut:-1], 'utf-8')
    swp = ''.join((i + (j or '') for (i, j) in zip_longest(code1, code2)))
    return swp