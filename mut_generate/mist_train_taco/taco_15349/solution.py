"""
QUESTION:
Do the following for a four-digit number N consisting of numbers 0-9.

1. Let L be the number obtained as a result of arranging the numerical values ​​of each of the N digits in descending order.
2. Let S be the number obtained as a result of arranging the numerical values ​​of each of the N digits in ascending order.
3. Let the difference L-S be the new N (end of one operation)
4. Repeat from 1. for the new N



At this time, it is known that any four-digit number will eventually become 6174, unless all digits are the same number (0000, 1111, etc.). For example, when N = 2012
First time (N = 2012): L = 2210, S = 0122, L-S = 2088
Second time (N = 2088): L = 8820, S = 0288, L-S = 8532
Third time (N = 8532): L = 8532, S = 2358, L-S = 6174
And reach 6174 in 3 operations.

Write a program that calculates how many operations will reach 6174 given a four-digit number consisting of the numbers 0-9.



input

The input consists of multiple datasets. The end of the input is indicated by 0000 on one line. Each dataset is given in the following format:


N


The dataset is one line and N (1 ≤ N ≤ 9999) indicates a four-digit number. If N <1000, the upper digit is padded with zeros.

The number of datasets does not exceed 10000.

output

The number of operations to reach 6174 for each data set is output on one line. However, if a number with all the same digits is given as input, NA is output.

Example

Input

6174
2012
3333
0000


Output

0
3
NA
"""

def calculate_operations_to_reach_6174(N):
    if N < 1000 or N > 9999:
        raise ValueError("N must be a four-digit number.")
    
    trial = 0
    while True:
        if N == 6174:
            return trial
        
        box = []
        original_N = N
        for _ in range(4):
            a = N % 10
            N = N // 10
            box.append(a)
        
        if box[0] == box[1] == box[2] == box[3]:
            return 'NA'
        
        box.sort()
        l = sum(box[i] * 10 ** i for i in range(4))
        box.sort(reverse=True)
        s = sum(box[i] * 10 ** i for i in range(4))
        
        N = l - s
        trial += 1