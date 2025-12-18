"""
QUESTION:
Given the time in numerals we may convert it into words, as shown below:  

$\begin{array}{l}5.00\rightarrow\:five \quad o'clock\\
5.01\rightarrow\:one\quad minute \quad past\quad five\\ 
5.10\rightarrow\:ten\quad minutes\quad past\quad five\\ 
5.15\rightarrow\:quarter\quad past\quad five\\ 5.30\rightarrow\:half\quad past\quad five\\ 5.40\rightarrow\:thenty\quad minutes\quad to\quad six\\ 
5.45\rightarrow\:quarter\quad to\quad six\\ 5.47\rightarrow\:thirteen\quad mimutes\quad to\quad six\\ 5.28\rightarrow\:twenty\quad eight\quad minutes\quad past\quad five\end{array}$


At $minutes=0$, use o' clock.  For $1\leq minutes\leq30$, use past, and for $30<minutes$ use to.  Note the space between the apostrophe and clock in o' clock.  Write a program which prints the time in words for the input given in the format described.  

Function Description  

Complete the timeInWords function in the editor below.  

timeInWords has the following parameter(s):  

int h: the hour of the day  
int m: the minutes after the hour  

Returns  

string: a time string as described  

Input Format

The first line contains $\mbox{h}$, the hours portion 
The second line contains $m$, the minutes portion  

Constraints

$1\leq h\leq12$  
$0\leq m<60$

Sample Input 0
5
47

Sample Output 0
thirteen minutes to six

Sample Input 1
3
00

Sample Output 1
three o' clock

Sample Input 2
7
15

Sample Output 2
quarter past seven
"""

def time_in_words(h, m):
    ones = 'one two three four five six seven eight nine'.split(' ')
    
    def num_to_word(x):
        if x < 10:
            return ones[x - 1]
        if x == 10:
            return 'ten'
        if x < 20:
            return 'eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split(' ')[x - 11]
        ten = x // 10
        one = x % 10
        tens = 'twenty thirty forty fifty'.split(' ')
        if one == 0:
            return tens[ten - 2]
        else:
            return tens[ten - 2] + ' ' + ones[one - 1]
    
    if m > 30:
        if m == 59:
            return 'one minute to %s' % num_to_word(h + 1 if h != 12 else 1)
        elif m == 45:
            return 'quarter to %s' % num_to_word(h + 1 if h != 12 else 1)
        else:
            return '%s minutes to %s' % (num_to_word(60 - m), num_to_word(h + 1 if h != 12 else 1))
    elif m == 0:
        return "%s o' clock" % num_to_word(h)
    elif m == 1:
        return 'one minute past %s' % num_to_word(h)
    elif m == 15:
        return 'quarter past %s' % num_to_word(h)
    elif m == 30:
        return 'half past %s' % num_to_word(h)
    else:
        return '%s minutes past %s' % (num_to_word(m), num_to_word(h))