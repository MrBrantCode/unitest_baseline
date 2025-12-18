"""
QUESTION:
Implement the [Polybius square cipher](http://en.wikipedia.org/wiki/Polybius_square).

Replace every letter with a two digit number. The first digit is the row number, and the second digit is the column number of following square. Letters `'I'` and `'J'` are both 24 in this cipher:


table#polybius-square {width: 100px;}
table#polybius-square td {background-color: #2f2f2f;}
table#polybius-square th {background-color: #3f3f3f;}


12345
1ABCDE
2FGHI/JK
3LMNOP
4QRSTU
5VWXYZ


Input will be valid (only spaces and uppercase letters from A to Z), so no need to validate them.

## Examples

```python
polybius('A')  # "11"
polybius('IJ') # "2424"
polybius('CODEWARS') # "1334141552114243"
polybius('POLYBIUS SQUARE CIPHER') # "3534315412244543 434145114215 132435231542"
```
"""

def polybius_cipher(text: str) -> str:
    letmap = {
        'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
        'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24',
        'K': '25', 'L': '31', 'M': '32', 'N': '33', 'O': '34',
        'P': '35', 'Q': '41', 'R': '42', 'S': '43', 'T': '44',
        'U': '45', 'V': '51', 'W': '52', 'X': '53', 'Y': '54',
        'Z': '55', ' ': ' '
    }
    
    encoded_text = ''.join(letmap[char] for char in text)
    return encoded_text