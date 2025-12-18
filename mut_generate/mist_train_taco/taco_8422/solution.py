"""
QUESTION:
She loves e-mail so much! She sends e-mails by her cellular phone to her friends when she has breakfast, she talks with other friends, and even when she works in the library! Her cellular phone has somewhat simple layout (Figure 1). Pushing button 1 once displays a character (’), pushing

<image>

it twice in series displays a character (,), and so on, and pushing it 6 times displays (’) again. Button 2 corresponds to charaters (abcABC), and, for example, pushing it four times displays (A). Button 3-9 have is similar to button 1. Button 0 is a special button: pushing it once make her possible to input characters in the same button in series. For example, she has to push “20202” to display “aaa” and “660666” to display “no”. In addition, pushing button 0 n times in series (n > 1) displays n − 1 spaces. She never pushes button 0 at the very beginning of her input. Here are some examples of her input and output:


666660666 --> No
44444416003334446633111 --> I’m fine.
20202202000333003330333 --> aaba f ff


One day, the chief librarian of the library got very angry with her and hacked her cellular phone when she went to the second floor of the library to return books in shelves. Now her cellular phone can only display button numbers she pushes. Your task is to write a program to convert the sequence of button numbers into correct characters and help her continue her e-mails!



Input

Input consists of several lines. Each line contains the sequence of button numbers without any spaces. You may assume one line contains no more than 10000 numbers. Input terminates with EOF.

Output

For each line of input, output the corresponding sequence of characters in one line.

Example

Input

666660666
44444416003334446633111
20202202000333003330333


Output

No
I'm fine.
aaba  f ff
"""

def decode_button_sequence(button_sequence: str) -> str:
    tbl = ['', "',.!?", 'abcABC', 'defDEF', 'ghiGHI', 'jklJKL', 'mnoMNO', 'pqrsPQRS', 'tuvTUV', 'wxyzWXYZ']
    
    ans = ''
    i = 0
    
    while i < len(button_sequence):
        c = button_sequence[i]
        w, d, i = 0, int(c), i + 1
        
        while i < len(button_sequence) and button_sequence[i] == c:
            i, w = i + 1, w + 1
        
        if d == 0:
            ans += ' ' * w
        else:
            ans += tbl[d][w % len(tbl[d])]
    
    return ans