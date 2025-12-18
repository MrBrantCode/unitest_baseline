"""
QUESTION:
A: Flick input

A college student who loves 2D, commonly known as 2D, replaced his long-used Galapagos mobile phone with a smartphone. 2D, who operated the smartphone for the first time, noticed that the character input method was a little different from that of old mobile phones. On smartphones, a method called flick input was adopted by taking advantage of the fact that the screen can be touch-flicked (flick means "the operation of sliding and flipping a finger on the screen"). Flick input is a character input method as shown below.

In flick input, as shown in Fig. A (a), input is performed using 10 buttons 0-9 (# and * are omitted this time). Each button is assigned one row-row row as shown in the figure.

<image>
---
Figure A: Smartphone button details

One button can be operated by the method shown in Fig. A (b). In other words

* If you just "touch" a button, the character "Adan" corresponding to that button will be output.
* Press the button "flick to the left" to output "Idan"
* When you press the button "flick upward", "Udan" is output.
* Press the button "flick to the right" to output "Edan"
* Press the button "flick down" to output "step"



That's what it means. Figure A (c) shows how to input flicks for all buttons. Note that you flick button 0 upwards to output "n".

Your job is to find the string that will be output as a result of a flick input operation, given a string that indicates that operation.

Input

A character string representing a flick input operation is given on one line (2 to 1000 characters). This character string consists of the numbers '0'-'9', which represent the buttons to be operated, and the five types of characters,'T',' L',' U',' R', and'D', which represent the flick direction. It consists of a combination.

The characters that represent the flick direction have the following meanings.

*'T': Just touch
*'L': Flick left
*'U': Flick up
*'R': Flick right
*'D': Flick down



For example, "2D" represents the operation of "flicking the button of 2 downward", so "ko" can be output.

In the given character string, one number and one character indicating the flick direction appear alternately. Also, it always starts with one number and ends with one letter indicating the flick direction. Furthermore, in Fig. A (c), flicking is not performed toward a place without characters (there is no input such as "8L").

Output

Output the character string representing the result of the flick input operation in Roman characters.

For romaji consonants,

* Or line:'k'
* Sayuki:'s'
* Ta line:'t'
* Line:'n'
* Is the line:'h'
* Ma line:'m'
* Ya line:'y'
* Line:'r'
* Wa line:'w'



to use. Romaji, which represents one hiragana character, should be output as a set of the consonants and vowels ('a','i','u','e','o') represented above. "shi" and "fu" are wrong because they violate this condition. However, the character "A line" should output only one vowel character, and "n" should output "n" twice in a row as "nn".

Output a line break at the end of the character string.

Sample Input 1


5R2D


Sample Output 1


neko


Sample Input 2


8U9U6U0T


Sample Output 2


yuruhuwa


Sample Input 3


9L4U7R1L2D0U4R3U4D


Sample Output 3


ritumeikonntesuto






Example

Input

5R2D


Output

neko
"""

def flick_input_to_romaji(input_string: str) -> str:
    flicks = {'T': 'a', 'L': 'i', 'U': 'u', 'R': 'e', 'D': 'o'}
    buttons = {'1': '', '2': 'k', '3': 's', '4': 't', '5': 'n', '6': 'h', '7': 'm', '8': 'y', '9': 'r', '0': 'w'}

    def get_word(button, flick):
        if button == '0' and flick == 'U':
            return 'nn'
        return buttons[button] + flicks[flick]

    result = ''
    for i in range(0, len(input_string), 2):
        result += get_word(input_string[i], input_string[i + 1])
    
    return result