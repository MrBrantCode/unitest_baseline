"""
QUESTION:
Efim just received his grade for the last test. He studies in a special school and his grade can be equal to any positive decimal fraction. First he got disappointed, as he expected a way more pleasant result. Then, he developed a tricky plan. Each second, he can ask his teacher to round the grade at any place after the decimal point (also, he can ask to round to the nearest integer). 

There are t seconds left till the end of the break, so Efim has to act fast. Help him find what is the maximum grade he can get in no more than t seconds. Note, that he can choose to not use all t seconds. Moreover, he can even choose to not round the grade at all.

In this problem, classic rounding rules are used: while rounding number to the n-th digit one has to take a look at the digit n + 1. If it is less than 5 than the n-th digit remain unchanged while all subsequent digits are replaced with 0. Otherwise, if the n + 1 digit is greater or equal to 5, the digit at the position n is increased by 1 (this might also change some other digits, if this one was equal to 9) and all subsequent digits are replaced with 0. At the end, all trailing zeroes are thrown away.

For example, if the number 1.14 is rounded to the first decimal place, the result is 1.1, while if we round 1.5 to the nearest integer, the result is 2. Rounding number 1.299996121 in the fifth decimal place will result in number 1.3.

Input

The first line of the input contains two integers n and t (1 ≤ n ≤ 200 000, 1 ≤ t ≤ 109) — the length of Efim's grade and the number of seconds till the end of the break respectively.

The second line contains the grade itself. It's guaranteed that the grade is a positive number, containing at least one digit after the decimal points, and it's representation doesn't finish with 0.

Output

Print the maximum grade that Efim can get in t seconds. Do not print trailing zeroes.

Examples

Input

6 1
10.245


Output

10.25


Input

6 2
10.245


Output

10.3


Input

3 100
9.2


Output

9.2

Note

In the first two samples Efim initially has grade 10.245. 

During the first second Efim can obtain grade 10.25, and then 10.3 during the next second. Note, that the answer 10.30 will be considered incorrect.

In the third sample the optimal strategy is to not perform any rounding at all.
"""

def maximize_grade(n: int, t: int, grade: str) -> str:
    s = list(grade)
    ind = n
    perenos = 0
    
    # Find the position of the decimal point
    for i in range(n):
        if s[i] == '.':
            nach = i + 1
            break
    
    # Find the first digit after the decimal point that is greater than 4
    for i in range(nach, n):
        if int(s[i]) > 4:
            ind = i
            break
    
    # If no digit greater than 4 is found, return the original grade
    if ind == n:
        return ''.join(s)
    
    # Perform rounding within the allowed seconds
    while t > 0 and s[ind] != '.':
        if int(s[ind]) > 3:
            ind -= 1
            perenos = 1
            t -= 1
            if s[ind] == '9':
                t += 1
        else:
            s[ind] = str(int(s[ind]) + 1)
            perenos = 0
            break
    
    # Handle rounding up to the integer part if necessary
    if s[ind] == '.':
        ind -= 1
        while s[ind] == '9':
            s[ind] = '0'
            ind -= 1
        if ind < 0 and perenos != 0:
            return '1' + ''.join(s)
        else:
            s[ind] = str(int(s[ind]) + perenos)
            return ''.join(s[:s.index('.')])
    else:
        while s[ind] == '9' or s[ind] == '.':
            if s[ind] == '.':
                ind -= 1
                continue
            s[ind] = '0'
            ind -= 1
        s[ind] = str(int(s[ind]) + perenos)
        return ''.join(s[:ind + 1])