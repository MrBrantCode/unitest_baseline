"""
QUESTION:
In this problem the input will consist of a number of lines of English text consisting of the letters of the English alphabet, the punctuation marks ' (apostrophe), . (full stop), , (comma), ; (semicolon), :(colon) and white space characters (blank, newline). Your task is print the words in the text in reverse order without any punctuation marks.
For example consider the following candidate for the input text:
$ $
This is a sample piece of text to illustrate this 
problem.  If you are smart you will solve this right.

$ $
The corresponding output would read as:
$ $
right this solve will you smart are you If problem
this illustrate to text of piece sample a is This

$ $
That is, the lines are printed in reverse order and in each line the words are printed in reverse order.

-----Input:-----
The first line of input contains a single integer $N$, indicating the number of lines in the input. This is followed by $N$ lines of input text.

-----Output:-----
$N$ lines of output text containing the input lines in reverse order and where each line contains the words in reverse order as illustrated above.

-----Constraints:-----
- $1 \leq N \leq 10000$.
- There are at most $80$ characters in each line

-----Sample input-----
2
This is a sample piece of text to illustrate this 
problem.  If you are smart you will solve this right.

-----Sample output-----
right this solve will you smart are you If problem
this illustrate to text of piece sample a is This
"""

def reverse_lines_and_words(N, lines):
    """
    Reverses the order of lines and words in each line of the input text.

    Parameters:
    - N (int): The number of lines in the input.
    - lines (list of str): A list of strings where each string is a line of text.

    Returns:
    - list of str: A list of strings where each string is a line of text in reverse order and with words in reverse order.
    """
    reversed_lines = []
    
    for j in range(N - 1, -1, -1):
        s = '` ' + lines[j]
        n = len(s) - 1
        y = s[n]
        f = ''
        
        while y != '`':
            w = ''
            while y != ' ':
                if ord(y) in range(97, 123) or ord(y) in range(65, 91):
                    w += y
                n -= 1
                y = s[n]
            wf = ''
            n -= 1
            y = s[n]
            x = len(w)
            for k in range(x):
                wf += w[x - k - 1]
            f += wf + ' '
        
        reversed_lines.append(f.strip())
    
    return reversed_lines