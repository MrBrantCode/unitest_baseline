"""
QUESTION:
Lucky numbers are those numbers which contain only "4" and/or "5". For example 4, 5, 44, 54,55,444 are lucky numbers while 457, 987 ,154 are not. 

Lucky number sequence is one in which all lucky numbers exist in increasing order for example   4,5,44,45,54,55,444,445,454,455... 

Now we concatenate all the lucky numbers (in ascending order) to make a lucky string  "4544455455444445454455..." 

Given n, your task is to find the nth digit of the lucky string.
If the digit is 4 then you have to print "Hacker" else you have to print "Earth".

Input:
first line contain number of test cases T , next T line contain a single interger n.

Output:
For each test case print "Hacker"(without quotes) if nth digit of lucky string is "4" else print "Earth"(without quotes) if nth digit of lucky string is "5". 

Constraints:
1 ≤ t ≤ 10^5
1 ≤ n ≤ 10^15

SAMPLE INPUT
4
1
2
3
9

SAMPLE OUTPUT
Hacker
Earth
Hacker
Earth
"""

import math

def find_nth_lucky_string_digit(n):
    maxLength = 0
    lastMax = maxLength
    numberOfDigit = 0
    
    while maxLength < n:
        lastMax = maxLength
        maxLength += math.pow(2, numberOfDigit) * numberOfDigit
        if maxLength >= n:
            break
        else:
            numberOfDigit += 1

    position = n - lastMax
    positionInNumber = numberOfDigit - position % numberOfDigit + 1 if position % numberOfDigit != 0 else 1
    numberPosition = math.ceil(position / numberOfDigit) - 1

    if numberPosition % math.pow(2, positionInNumber) < math.pow(2, positionInNumber - 1):
        return 'Hacker'
    else:
        return 'Earth'