"""
QUESTION:
Special Numbers 
Mani has encountered a problem on Special numbers in Bytecode. A number S is called a special number if its digits are in an arithmetic progression modulo 10. He has an array consisting of all numbers from 1 to N and needs your help to find the number of special numbers in the array. He has promised you a significant share of the prize money if he wins the contest :p 
Note:
123,99,802 are special numbers.
146 is not a special number 

-----Input-----

Input consists of 1 integer - the value of N

-----Output-----
Print one integer in the first line - the solution to this problem

-----Constraints-----
- 1 ≤ Number of digits in N ≤ 105

Example

Input

123

Output

102
"""

def count_special_numbers(N):
    n = str(N)
    x = len(n)
    no = list(map(int, n))
    temp = [0] * x
    
    if x > 2:
        sum = 99
        for i in range(3, x):
            sum = sum + 90
        sum = sum + 10 * (int(n[0]) - 1)
        sum = sum + int(n[1])
        f = int(n[0]) % 10
        s = int(n[1]) % 10
        cd = s - f
        temp[0] = n[0]
        temp[1] = n[1]
        for i in range(2, x):
            nxt = (s + cd) % 10
            temp[i] = chr(nxt + 48)
            s = nxt
        temp = list(map(int, temp))
        if temp <= no:
            sum = sum + 1
        return sum
    else:
        return int(n)