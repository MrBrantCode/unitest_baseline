"""
QUESTION:
Seryozha has a very changeable character. This time he refused to leave the room to Dima and his girlfriend (her hame is Inna, by the way). However, the two lovebirds can always find a way to communicate. Today they are writing text messages to each other.

Dima and Inna are using a secret code in their text messages. When Dima wants to send Inna some sentence, he writes out all words, inserting a heart before each word and after the last word. A heart is a sequence of two characters: the "less" characters (<) and the digit three (3). After applying the code, a test message looks like that: <3word_1<3word_2<3 ... word_{n}<3.

Encoding doesn't end here. Then Dima inserts a random number of small English characters, digits, signs "more" and "less" into any places of the message.

Inna knows Dima perfectly well, so she knows what phrase Dima is going to send her beforehand. Inna has just got a text message. Help her find out if Dima encoded the message correctly. In other words, find out if a text message could have been received by encoding in the manner that is described above.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 10^5) — the number of words in Dima's message. Next n lines contain non-empty words, one word per line. The words only consist of small English letters. The total length of all words doesn't exceed 10^5. 

The last line contains non-empty text message that Inna has got. The number of characters in the text message doesn't exceed 10^5. A text message can contain only small English letters, digits and signs more and less.


-----Output-----

In a single line, print "yes" (without the quotes), if Dima decoded the text message correctly, and "no" (without the quotes) otherwise.


-----Examples-----
Input
3
i
love
you
<3i<3love<23you<3

Output
yes

Input
7
i
am
not
main
in
the
family
<3i<>3am<3the<3<main<3in<3the<3><3family<3

Output
no



-----Note-----

Please note that Dima got a good old kick in the pants for the second sample from the statement.
"""

def is_message_encoded_correctly(n, words, encoded_message):
    stage = 0
    cur = 0
    curpos = 0
    f = 0
    
    for j in range(len(encoded_message)):
        i = encoded_message[j]
        curword = words[cur]
        
        if stage == 0 and i == '<':
            stage = 1
        elif stage == 1 and i == '3':
            stage = 2
        
        if stage == 2:
            if i == curword[curpos]:
                curpos += 1
            if curpos == len(curword):
                cur += 1
                curpos = 0
                stage = 0
                if cur == len(words):
                    for k in range(j + 1, len(encoded_message)):
                        if encoded_message[k] == '<' and f == 0:
                            f = 1
                        if encoded_message[k] == '3' and f == 1:
                            f = 2
                    break
    
    if cur == len(words) and f == 2:
        return 'yes'
    else:
        return 'no'