"""
QUESTION:
Atish is very talkative. He just doesn't stop speaking. Unfortunately for those around him, he's also a maths wiz, and befuddles anyone who dares speak to him. Annoyed with this, Souradeep asked him to shut up, to which Atish replied, 
Take a number, x, find its factorial,  remove the zeroes, and find the last digit. Call this the "Atish digit". When you can do this fast enough to satisfy me, I'll shut up. 
Now Souradeep is not a mathlete. So he's come to you for help. Can you help him shut Atish up?

EDIT
Maximum number of test cases - 500,
x<10000

SAMPLE INPUT
5

0
1
24
13
87

SAMPLE OUTPUT
1
1
6
8
4
"""

def get_atish_digit(x: int) -> int:
    if x >= 10000:
        raise ValueError("Input number should be less than 10000")
    
    a = 1
    eps = 10**30
    
    for i in range(2, x + 1):
        te = i
        while te % 10 == 0:
            te //= 10
        a *= te
        while a % 10 == 0:
            a //= 10
        a %= eps
    
    return a % 10