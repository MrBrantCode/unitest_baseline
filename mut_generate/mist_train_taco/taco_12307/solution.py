"""
QUESTION:
Alice wants to send an email to Miku on her mobile phone.

The only buttons that can be used for input on mobile phones are number buttons. Therefore, in order to input characters, the number buttons are pressed several times to input characters. The following characters are assigned to the number buttons of the mobile phone, and the confirmation button is assigned to button 0. With this mobile phone, you are supposed to press the confirm button after you finish entering one character.

* 1:.,!? (Space)
* 2: a b c
* 3: d e f
* 4: g h i
* 5: j k l
* 6: m n o
* 7: p q r s
* 8: t u v
* 9: w x y z
* 0: Confirm button


For example, if you press button 2, button 2, or button 0, the letter changes from'a'to'b', and the confirm button is pressed here, so the letter b is output. If you enter the same number in succession, the changing characters will loop. That is, if you press button 2 five times and then button 0, the letters change from'a'→' b'→'c' →'a' →'b', and the confirm button is pressed here. 'b' is output.

You can press the confirm button when no button is pressed, but in that case no characters are output.

Your job is to recreate the message Alice created from a row of buttons pressed by Alice.



Input

The first line gives the number of test cases. Each test case is then given a string of digits up to 1024 in length in one row.

Output

Print the string of Alice's message line by line for each test case. However, you can assume that the output is one or more and less than 76 characters.

Example

Input

5
20
220
222220
44033055505550666011011111090666077705550301110
000555555550000330000444000080000200004440000


Output

a
b
b
hello, world!
keitai
"""

def decode_mobile_message(test_cases):
    keylist = [
        [], 
        ['.', ',', '!', '?', ' '], 
        ['a', 'b', 'c'], 
        ['d', 'e', 'f'], 
        ['g', 'h', 'i'], 
        ['j', 'k', 'l'], 
        ['m', 'n', 'o'], 
        ['p', 'q', 'r', 's'], 
        ['t', 'u', 'v'], 
        ['w', 'x', 'y', 'z']
    ]
    
    decoded_messages = []
    
    for case in test_cases:
        output = ''
        for item in case.split('0'):
            if item == '':
                continue
            key = int(item[0])
            output += keylist[key][len(item) % len(keylist[key]) - 1]
        decoded_messages.append(output)
    
    return decoded_messages