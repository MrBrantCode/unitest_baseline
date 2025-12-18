"""
QUESTION:
Slugtera is a town where three types of people lives which are  criminals , terminator and life saver . Criminals are represented by o and terminator are represented by x and saver are represented by * . So in this story x function is to kill all o but however if * comes between o    and  x   then x  is not able to kill o .

Input :
The first line contains T - number  of test cases . Each of next T lines contain a string S.

Output :
For each test case you need to print the result after reduction .

Constraints :
1 ≤ T ≤ 50
1 ≤ |S| ≤ 100, where |S| denotes the length of string S.

Note : String will contain only small characters.

SAMPLE INPUT
3
oxox
xo*oooooooo*xo
ooooooooo*xooo***xxxxooooo

SAMPLE OUTPUT
xx
x*oooooooo*x
ooooooooo*x***xxxx

Explanation

In the first case  : o is terminated by x.

In the second case :  many O's are saved because of * pair.

In the third case  : The starting O's are saved because * is between o and x.
"""

def reduce_string_for_slugtera(T, strings):
    results = []
    
    for s in strings:
        if 'x' not in s or 'o' not in s:
            results.append(s)
        elif '*' not in s and 'o' in s:
            results.append(s.replace('o', ''))
        elif '*' in s:
            s2 = ''
            for char in s:
                if char == '*':
                    s2 += '.' + char + '.'
                else:
                    s2 += char
            parts = s2.split('.')
            reduced_parts = []
            for part in parts:
                if part == "":
                    continue
                elif 'x' in part and 'o' in part:
                    reduced_parts.append(part.replace('o', ''))
                else:
                    reduced_parts.append(part)
            results.append(''.join(reduced_parts))
    
    return results