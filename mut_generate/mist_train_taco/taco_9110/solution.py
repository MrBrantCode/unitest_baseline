"""
QUESTION:
A sequence of integers is called a wonderful sequence if all the integers in it are positive and it is a strictly increasing sequence.

Given a sequence of integers, you have to make it a wonderful sequence. For that you can change any element you want, but you should make as less changes as possible in order to make it a wonderful sequence.

Input

The first line of input is an integer T(T ≤ 5), the number of test cases. Each test case contains 2 lines.

The first line of the test case contains an integer (0 < N ≤ 100000), i.e. the number of elements in the original sequence.

The second line contains N positive integers, no larger than 2000000000, which forms the original sequence.

Output

For each test case output the minimal number of elements you must change in the original sequence to make it a wonderful sequence.

SAMPLE INPUT
3
2
1 2
3
3 2 1
5
10 5 6 7 8

SAMPLE OUTPUT
0
2
1

Explanation

For the 1st test case you needn't to change any elements.
For the 2nd test case you can change 3 into 1 and change 1 into 3.
For the 3rd test case you can change 10 into 1.
"""

def min_changes_to_wonderful_sequence(sequence):
    n = len(sequence)
    if n == 0:
        return 0
    
    change = 0
    min_val = 0
    max_val = 2000000000
    
    i = 0
    j = n - 1
    
    while i < n and j >= 0 and i <= j:
        if j - i == 1:
            if sequence[i] < sequence[j]:
                break
            else:
                sequence[i] = min_val
                change += 1
                break
        
        elif i != j:
            if sequence[j] - sequence[i] < j - i - 1:
                if sequence[j] - j < 0:
                    sequence[j] = max_val
                    max_val -= 1
                    j -= 1
                else:
                    sequence[i] = min_val
                    min_val += 1
                    i += 1
                change += 1
            else:
                min_val = sequence[i] + 1
                max_val = sequence[j] - 1
                
                if sequence[i] > sequence[i + 1]:
                    sequence[i + 1] = min_val
                    min_val += 1
                    change += 1
                    i += 1
                else:
                    i += 1
                if sequence[j] < sequence[j - 1]:
                    sequence[j - 1] = max_val
                    max_val -= 1
                    change += 1
                    j -= 1
        else:
            if sequence[i] < sequence[i + 1]:
                if sequence[i] < sequence[i - 1]:
                    sequence[i] = min_val
                    change += 1
            else:
                sequence[i] = max_val
                change += 1
    
    return change