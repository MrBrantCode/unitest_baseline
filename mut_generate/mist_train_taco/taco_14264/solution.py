"""
QUESTION:
You have successfully completed your studies and are preparing to move from near Komaba to near Hongo. As I was organizing my house, I found a lot of lottery tickets I bought last year. After confirming the exchange deadline, I have to cash in by tomorrow, but it is troublesome to go to the lottery counter for a small amount of money because I am not ready to move at all. So you decide to find out how much you can win.

The lottery consists of eight digits. The winning number is also composed of 8 digits and a number and'*', and if the lottery you have and the number part match, the winning money will be paid according to the winning number.

For example, if the lottery number you have is "12345678", you will win if the winning number is "******* 8" or "**** 5678", but the winning number is "**". If it is ** 4678 ", you will not win. There can be multiple winning numbers, and the winnings will be paid independently for each. However, the winning numbers are chosen so that one lottery does not win more than one winning number. For example, if there are two winning numbers, "******* 8" and "**** 5678", "12345678" will win both, so such a winning number will be selected. There is no one to be done.

Your job is to write a program that outputs how much winning money you will get for the lottery number you have and the lottery winning number given as input.

Notes on Test Cases

Multiple datasets are given in the above input format. Create a program that outputs each data set in the above output format.

When n is 0, it indicates the end of input.

<!-



Input

The input is given in the following format.


n m
N1 M1
...
Nn Mn
B1
...
Bm

In the first line, the number of winning numbers n (1 ≤ n ≤ 100) and the number of lottery tickets in possession m (1 ≤ m ≤ 1000) are given as integers.

In the next n lines, each line is given a winning number Ni and a winnings Mi (1 ≤ Mi ≤ 1000000). Winnings are integers. The format of the winning number is as described in the question text.

The next m lines will give you the number of the lottery you have.

Output

Output the total amount of winnings.

Examples

Input

3 3
*******1 100
******22 1000
11111112 1000000
01203291
02382022
11111111
10 10
****3228 149416
****3992 198635
****4286 77783
****4843 225244
***49835 231046
***59393 379996
*5763748 437345
*6726222 58054
*8117882 16375
*9244339 537727
77885716
96726222
26971031
66652868
89599648
37772338
64679621
65479161
92959393
57855682
0 0


Output

1200
438050


Input

3 3
*******1 100
******22 1000
11111112 1000000
01203291
02382022
11111111


Output

1200


Input

10 10
****3228 149416
****3992 198635
****4286 77783
****4843 225244
***49835 231046
***59393 379996
*5763748 437345
*6726222 58054
*8117882 16375
*9244339 537727
77885716
96726222
26971031
66652868
89599648
37772338
64679621
65479161
92959393
57855682


Output

438050
"""

import re

def calculate_total_winnings(winning_numbers, lottery_tickets):
    total_winnings = 0
    
    # Compile the winning number patterns into regex objects
    compiled_patterns = []
    for pattern, winnings in winning_numbers:
        regex_pattern = pattern.replace('*', '[0-9]')
        compiled_patterns.append((re.compile(regex_pattern), winnings))
    
    # Check each lottery ticket against the compiled patterns
    for ticket in lottery_tickets:
        for pattern, winnings in compiled_patterns:
            if pattern.search(ticket):
                total_winnings += winnings
                break
    
    return total_winnings