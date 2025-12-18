"""
QUESTION:
The Earth has been invaded by aliens. They demand our beer and threaten to destroy the Earth if we do not supply the exact number of beers demanded.

Unfortunately, the aliens only speak Morse code. Write a program to convert morse code into numbers using the following convention:

1 .----
2 ..---
3 ...--
4 ....-
5 .....
6 -....
7 --...
8 ---..
9 ----.
0 -----
"""

def morse_to_number(morse_code: str) -> int:
    MORSE_TO_NUM = {
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0'
    }
    
    # Ensure the length of morse_code is a multiple of 5
    if len(morse_code) % 5 != 0:
        raise ValueError("Invalid Morse code length. It should be a multiple of 5.")
    
    # Convert the Morse code to a number
    number_str = ''.join(MORSE_TO_NUM[morse_code[i:i + 5]] for i in range(0, len(morse_code), 5))
    
    return int(number_str)