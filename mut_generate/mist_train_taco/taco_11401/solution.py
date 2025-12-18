"""
QUESTION:
One day, Taro received a strange email with only the number "519345213244" in the text. The email was from my cousin, who was 10 years older than me, so when I called and asked, "Oh, I sent it with a pocket bell because I was in a hurry. It's convenient. Nice to meet you!" I got it. You know this cousin, who is always busy and a little bit aggressive, and when you have no choice but to research "pager hitting" yourself, you can see that it is a method of input that prevailed in the world about 10 years ago. I understand.

In "Pokebell Strike", enter one character with two numbers, such as 11 for "A" and 15 for "O" according to the conversion table shown in Fig. 1. For example, to enter the string "Naruto", type "519345". Therefore, any letter can be entered with two numbers.

<image>

Figure 1

When mobile phones weren't widespread, high school students used this method to send messages from payphones to their friends' pagers. Some high school girls were able to pager at a tremendous speed. Recently, my cousin, who has been busy with work, has unknowingly started typing emails with a pager.

Therefore, in order to help Taro who is having a hard time deciphering every time, please write a program that converts the pager message into a character string and outputs it. However, the conversion table shown in Fig. 2 is used for conversion, and only lowercase letters, ".", "?", "!", And blanks are targeted. Output NA for messages that contain characters that cannot be converted.

<image>

Figure 2



Input

Multiple messages are given. One message (up to 200 characters) is given on each line. The total number of messages does not exceed 50.

Output

For each message, output the converted message or NA on one line.

Example

Input

341143514535
314
143565553551655311343411652235654535651124615163
551544654451431564
4
3411
6363636363
153414


Output

naruto
NA
do you wanna go to aizu?
yes sure!
NA
na
?????
end
"""

def decode_pager_message(message: str) -> str:
    mes = {
        11: 'a', 12: 'b', 13: 'c', 14: 'd', 15: 'e',
        21: 'f', 22: 'g', 23: 'h', 24: 'i', 25: 'j',
        31: 'k', 32: 'l', 33: 'm', 34: 'n', 35: 'o',
        41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't',
        51: 'u', 52: 'v', 53: 'w', 54: 'x', 55: 'y',
        61: 'z', 62: '.', 63: '?', 64: '!', 65: ' '
    }
    
    # Check if the message length is odd, which is invalid
    if len(message) % 2 != 0:
        return "NA"
    
    decoded_message = ""
    
    for i in range(0, len(message), 2):
        key = int(message[i:i + 2])
        if key in mes:
            decoded_message += mes[key]
        else:
            return "NA"
    
    return decoded_message