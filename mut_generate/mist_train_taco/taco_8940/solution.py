"""
QUESTION:
My arm is stuck and I can't pull it out.

I tried to pick up something that had rolled over to the back of my desk, and I inserted my arm while illuminating it with the screen of my cell phone instead of a flashlight, but I accidentally got caught in something and couldn't pull it out. It hurts if you move it forcibly.

What should I do. How can I escape? Do you call for help out loud? I'm embarrassed to dismiss it, but it seems difficult to escape on my own. No, no one should have been within reach. Hold down your impatience and look around. If you can reach that computer, you can call for help by email, but unfortunately it's too far away. After all, do we have to wait for someone to pass by by chance?

No, wait, there is a machine that sends emails. It's already in your hands, rather than within reach. The screen at the tip of my deeply extended hand is blurry and hard to see, but it's a mobile phone I've been using for many years. You should be able to send emails even if you can't see the screen.

Carefully press the button while drawing the screen in your head. Rely on the feel of your finger and type in a message by pressing the number keys many times to avoid making typos. It doesn't convert to kanji, and it should be transmitted even in hiragana. I'm glad I didn't switch to the mainstream smartphones for the touch panel.

Take a deep breath and put your finger on the send button. After a while, my cell phone quivered lightly. It is a signal that the transmission is completed. sigh. A friend must come to help after a while.

I think my friends are smart enough to interpret it properly, but the message I just sent may be different from the one I really wanted to send. The character input method of this mobile phone is the same as the widely used one, for example, use the "1" button to input the hiragana of the "A" line. "1" stands for "a", "11" stands for "i", and so on, "11111" stands for "o". Hiragana loops, that is, "111111" also becomes "a". The "ka" line uses "2", the "sa" line uses "3", ..., and the behavior when the same button is pressed in succession is the same as in the example of "1".

However, this character input method has some annoying behavior. If you do not operate for a while after pressing the number button, the conversion to hiragana will be forced. In other words, if you press "1" three times in a row, it will become "U", but if you press "1" three times after a while, it will become "Ah". To give another example, when you press "111111", the character string entered depends on the interval between the presses, which can be either "a" or "ah ah ah". "111111111111" may be "yes", "yeah ah", or twelve "a". Note that even if you press a different number button, it will be converted to hiragana, so "12345" can only be the character string "Akasatana".

Well, I didn't mean to press the wrong button because I typed it carefully, but I'm not confident that I could press the buttons at the right intervals. It's very possible that you've sent something different than the message you really wanted to send. Now, how many strings may have been sent? Oh, this might be a good way to kill time until a friend comes to help. They will come to help within 5 hours at the latest. I hope it can be solved by then.



Input

The input consists of multiple cases.
Each case is given in the following format.


string


The end of the input is given by the line where the input consists of "#"

string contains up to 100,000 numbers between 0 and 9.
No more than 50 inputs have a string length greater than 10,000.


The test case file size is guaranteed to be 5MB or less.
Also, the number of test cases does not exceed 100.


The characters that can be entered with each number key are as shown in the table below.

Numbers | Enterable characters
--- | ---
1 | Aiueo
2 | Kakikukeko
3 |
4 |
5 | What is it?
6 | Hahifuheho
7 | Mamimumemo
8 | Yayuyo
9 | Larry Lero
0 | Won

Output

Divide how to interpret the sentence by 1000000007 and output the remainder on one line.

Examples

Input

1
11
111111
111111111111
12345
11111111119999999999
11111111113333333333
11111111118888888888
11111111112222222222111111111
11111111110000000000444444444
11224111122411
888888888888999999999999888888888888999999999999999999
666666666666666777333333333338888888888
1111114444441111111444499999931111111222222222222888111111115555
#


Output

1
2
32
1856
1
230400
230400
156480
56217600
38181120
128
26681431
61684293
40046720


Input

1
11
111111
111111111111
12345
11111111119999999999
11111111113333333333
11111111118888888888
11111111112222222222111111111
11111111110000000000444444444
11224111122411
888888888888999999999999888888888888999999999999999999
666666666666666777333333333338888888888
1111114444441111111444499999931111111222222222222888111111115555


Output

1
2
32
1856
1
230400
230400
156480
56217600
38181120
128
26681431
61684293
40046720
"""

def f3(n):
    a = b = c = 0
    for _ in range(n):
        (a, b, c) = ((a + b + c + 1) % 1000000007, a, b)
    return a

def f5(n):
    a = b = c = d = e = 0
    for _ in range(n):
        (a, b, c, d, e) = ((a + b + c + d + e + 1) % 1000000007, a, b, c, d)
    return a

def calculate_possible_strings(input_string):
    ans = 1
    num = '_'
    cnt = 1
    
    for n in input_string + '_':
        if n == num:
            cnt += 1
        else:
            if num in '80':
                ans = ans * f3(cnt) % 1000000007
            else:
                ans = ans * f5(cnt) % 1000000007
            num = n
            cnt = 1
    
    return ans